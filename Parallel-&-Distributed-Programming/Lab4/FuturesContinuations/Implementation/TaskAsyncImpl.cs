/*
 * The connect/send/receive operations are wrapped in tasks, with the callback setting the result of the task.
 * The async/await mechanism is used.
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
    class TaskAsyncImpl
    {
        private static List<string> hosts;
        public static void run(List<string> hostnames)
        {
            hosts = hostnames;
            var tasks = new List<Task>();

            for (var i = 0; i < hostnames.Count; i++)
                    tasks.Add(Task.Factory.StartNew(DoStartAsync, i));

            Task.WaitAll(tasks.ToArray());
        }

        private static void DoStartAsync(object idObject)
        {
            var id = (int)idObject;

            StartAsyncClient(hosts[id], id);
        }

        private static async void StartAsyncClient(string host, int id)   // now functions are 'async'
        {
            var ipHostInfo = Dns.GetHostEntry(host.Split('/')[0]);
            var ipAddress = ipHostInfo.AddressList[0];
            var remoteEndpoint = new IPEndPoint(ipAddress, ReqParser.PORT);

            // create the TCP/IP socket
            var client = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp); // client socket

            var requestSocket = new CustomSocket
            {
                sock = client,
                hostname = host.Split('/')[0],
                endpoint = host.Contains("/") ? host.Substring(host.IndexOf("/", StringComparison.Ordinal)) : "/",
                remoteEndPoint = remoteEndpoint,
                id = id
            }; // state object

            await ConnectAsync(requestSocket); // connect to remote server (await instead of .Wait())

            await SendAsync(requestSocket, ReqParser.GetRequestString(requestSocket.hostname, requestSocket.endpoint)); // request data from the server

            await ReceiveAsync(requestSocket); // receive server response

            Console.WriteLine("Connection {0} > Content length is: {1}\n", requestSocket.id, ReqParser.GetContentLen(requestSocket.responseContent.ToString()));

            // release the socket
            client.Shutdown(SocketShutdown.Both);
            client.Close();
        }

        private static async Task ConnectAsync(CustomSocket state)
        {
            state.sock.BeginConnect(state.remoteEndPoint, ConnectCallback, state);

            await Task.FromResult<object>(state.connectDone.WaitOne()); // block until signaled
        }

        private static void ConnectCallback(IAsyncResult ar)
        {
            // retrieve the details from the connection information wrapper
            var resultSocket = (CustomSocket)ar.AsyncState;
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;
            var hostname = resultSocket.hostname;

            clientSocket.EndConnect(ar); // complete connection

            Console.WriteLine("Connection {0} > Socket connected to {1} ({2})\n", clientId, hostname, clientSocket.RemoteEndPoint);

            resultSocket.connectDone.Set(); // signal connection is up
        }

        private static async Task SendAsync(CustomSocket state, string data)
        {
            var byteData = Encoding.ASCII.GetBytes(data);

            // send data
            state.sock.BeginSend(byteData, 0, byteData.Length, 0, SendCallback, state);

            await Task.FromResult<object>(state.sendDone.WaitOne());
        }

        private static void SendCallback(IAsyncResult ar)
        {
            var resultSocket = (CustomSocket)ar.AsyncState;
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;

            var bytesSent = clientSocket.EndSend(ar); // complete sending the data to the server  

            Console.WriteLine("Connection {0} > Sent {1} bytes to server.\n", clientId, bytesSent);

            resultSocket.sendDone.Set(); // signal that all bytes have been sent
        }

        private static async Task ReceiveAsync(CustomSocket state)
        {
            // receive data
            state.sock.BeginReceive(state.buffer, 0, CustomSocket.BUFF_SIZE, 0, ReceiveCallback, state);

            await Task.FromResult<object>(state.receiveDone.WaitOne());
        }

        private static void ReceiveCallback(IAsyncResult ar)
        {
            // retrieve the details from the connection information wrapper
            var resultSocket = (CustomSocket)ar.AsyncState;
            var clientSocket = resultSocket.sock;

            try
            {
                // read data from the remote device.  
                var bytesRead = clientSocket.EndReceive(ar);

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
