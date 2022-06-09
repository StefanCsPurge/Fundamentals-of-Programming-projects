/*
 * The connect/send/receive operations are wrapped in tasks, with the callback setting the result of the task.
 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading.Tasks;
using FuturesContinuations.Utils;

namespace FuturesContinuations.Implementation
{
    class TaskImpl
    {
        private static List<string> hosts;
        public static void run(List<string> hostnames)
        {
            hosts = hostnames;
            var tasks = new List<Task>();

            for (var i = 0; i < hostnames.Count; i++)   // start the threads
                    tasks.Add(Task.Factory.StartNew(DoStart, i));    
            Task.WaitAll(tasks.ToArray());
        }

        private static void DoStart(object idObject)
        {
            var id = (int)idObject;
            StartClient(hosts[id], id);
        }

        /// create client socket, start the connection, send reqest, get response, get result
        private static void StartClient(string host, int id)
        {
            var ipHostInfo = Dns.GetHostEntry(host.Split('/')[0]);
            var ipAddr = ipHostInfo.AddressList[0];
            var remEndPoint = new IPEndPoint(ipAddr, ReqParser.PORT);

            var client = new Socket(ipAddr.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            var requestSocket = new CustomSocket
            {
                sock = client,
                hostname = host.Split('/')[0],
                endpoint = host.Contains("/") ? host.Substring(host.IndexOf("/", StringComparison.Ordinal)) : "/",
                remoteEndPoint = remEndPoint,
                id = id
            };

            Connect(requestSocket).Wait(); // connect to remote server

            Send(requestSocket, ReqParser.GetRequestString(requestSocket.hostname, requestSocket.endpoint)).Wait(); // request data from server
            
            Receive(requestSocket).Wait(); // receive server response

            Console.WriteLine("Connection {0} > Content length is: {1}\n", requestSocket.id, ReqParser.GetContentLen(requestSocket.responseContent.ToString()));

            // release the socket
            client.Shutdown(SocketShutdown.Both);
            client.Close();
        }

        private static Task Connect(CustomSocket state)
        {
            state.sock.BeginConnect(state.remoteEndPoint, ConnectCallback, state);

            return Task.FromResult(state.connectDone.WaitOne()); // block until signaled
        }

        private static void ConnectCallback(IAsyncResult rs)
        {
            // retrieve the details from the connection information wrapper
            var resultSocket = (CustomSocket)rs.AsyncState;
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;
            var hostname = resultSocket.hostname;

            clientSocket.EndConnect(rs); // complete connection

            Console.WriteLine("Connection {0} > Socket connected to {1} ({2})\n", clientId, hostname, clientSocket.RemoteEndPoint);

            resultSocket.connectDone.Set(); // signal connection is up
        }


        private static Task Send(CustomSocket state, string data)
        {
            // convert the string data to byte data using ASCII encoding.  
            var byteData = Encoding.ASCII.GetBytes(data);

            // send data  
            state.sock.BeginSend(byteData, 0, byteData.Length, 0, SendCallback, state);

            return Task.FromResult(state.sendDone.WaitOne());
        }

        private static void SendCallback(IAsyncResult rs)
        {
            var resultSocket = (CustomSocket)rs.AsyncState;
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;

            var bytesSent = clientSocket.EndSend(rs); // complete sending the data to the server  

            Console.WriteLine("Connection {0} > Sent {1} bytes to server.\n", clientId, bytesSent);

            resultSocket.sendDone.Set(); // signal that all bytes have been sent
        }

        private static Task Receive(CustomSocket state)
        {
            // receive data
            state.sock.BeginReceive(state.buffer, 0, CustomSocket.BUFF_SIZE, 0, ReceiveCallback, state);

            return Task.FromResult(state.receiveDone.WaitOne());
        }

        private static void ReceiveCallback(IAsyncResult rs)
        {
            // retrieve the details from the connection information wrapper
            var resultSocket = (CustomSocket)rs.AsyncState;
            var clientSocket = resultSocket.sock;

            try
            {
                // read data from the remote device.  
                var bytesRead = clientSocket.EndReceive(rs);

                // get from the buffer, a number of characters <= to the buffer size, and store it in the responseContent
                resultSocket.responseContent.Append(Encoding.ASCII.GetString(resultSocket.buffer, 0, bytesRead));

                // if the response header has not been fully obtained, get the next chunk of data
                if (!ReqParser.ResponseHeaderObtained(resultSocket.responseContent.ToString()))
                {
                    clientSocket.BeginReceive(resultSocket.buffer, 0, CustomSocket.BUFF_SIZE, 0, ReceiveCallback, resultSocket);
                }
                else
                {
                    resultSocket.receiveDone.Set(); // signal that all bytes have been received       
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

        }

    }
}
