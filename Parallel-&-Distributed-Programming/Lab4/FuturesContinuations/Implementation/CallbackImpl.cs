/*
 * The parser is directly implemented on the callbacks (event-driven);
 */
using FuturesContinuations.Utils;
using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace FuturesContinuations.Implementation
{
    class CallbackImpl
    {
        public static void run(List<string> hostnames)
        {
            for (var i = 0; i < hostnames.Count; i++)
            {
                StartClient(hostnames[i], i);
                Thread.Sleep(420);
            }
        }

        /// create client socket and start the connection
        private static void StartClient(string host, int id)
        {
            var ipHostInfo = Dns.GetHostEntry(host.Split('/')[0]); // get host dns entry
            var ipAddress = ipHostInfo.AddressList[0]; // separate ip of host
            var remoteEndpoint = new IPEndPoint(ipAddress, ReqParser.PORT); // create endpoint
            // Console.WriteLine(remoteEndpoint);
            var client = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp); // create client socket

            var requestSocket = new CustomSocket
            {
                sock = client,
                hostname = host.Split('/')[0],
                endpoint = host.Contains("/") ? host.Substring(host.IndexOf("/")) : "/",
                remoteEndPoint = remoteEndpoint,
                id = id
            }; // build my custom socket

            requestSocket.sock.BeginConnect(requestSocket.remoteEndPoint, Connected, requestSocket); // connect to the remote endpoint  
        }

        /// establish connection and begin get reqest send
        private static void Connected(IAsyncResult rs)
        {
            var resultSocket = (CustomSocket)rs.AsyncState; // conn state
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;
            var hostname = resultSocket.hostname;
            var endpoint = resultSocket.endpoint;

            clientSocket.EndConnect(rs); // end connection
            Console.WriteLine("Connection {0} : Socket connected to {1}{2} ({3})", clientId, hostname, endpoint, clientSocket.RemoteEndPoint);

            var byteData = Encoding.ASCII.GetBytes(ReqParser.GetRequestString(resultSocket.hostname, resultSocket.endpoint));
            //Console.WriteLine(Encoding.Default.GetString(byteData));
            resultSocket.sock.BeginSend(byteData, 0, byteData.Length, 0, Sent, resultSocket);
        }

        /// begin receiving the response
        private static void Sent(IAsyncResult rs)
        {
            var resultSocket = (CustomSocket)rs.AsyncState;
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;

            // send data to server
            var bytesSent = clientSocket.EndSend(rs);
            Console.WriteLine("Connection {0} -> Sent {1} bytes to server.", clientId, bytesSent);

            // server response (data)
            resultSocket.sock.BeginReceive(resultSocket.buffer, 0, CustomSocket.BUFF_SIZE, 0, Receiving, resultSocket);
        }

        /// get needed data from the response
        private static void Receiving(IAsyncResult rs)
        {
            // get answer details
            var resultSocket = (CustomSocket)rs.AsyncState;
            var clientSocket = resultSocket.sock;
            var clientId = resultSocket.id;

            try
            {
                var bytesRead = clientSocket.EndReceive(rs); // read response data

                resultSocket.responseContent.Append(Encoding.ASCII.GetString(resultSocket.buffer, 0, bytesRead));
                // Console.WriteLine(resultSocket.responseContent.ToString());

                // if the response header has not been fully obtained, get the next chunk of data
                if (!ReqParser.ResponseHeaderObtained(resultSocket.responseContent.ToString()))
                {
                    clientSocket.BeginReceive(resultSocket.buffer, 0, CustomSocket.BUFF_SIZE, 0, Receiving, resultSocket);
                }
                else
                {
                    Console.WriteLine("Content length is: {0} <- received\n" +
                                      "-------------------------------\n", ReqParser.GetContentLen(resultSocket.responseContent.ToString()));

                    clientSocket.Shutdown(SocketShutdown.Both); // free socket
                    clientSocket.Close();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
