﻿using System;

namespace FuturesContinuations.Utils
{
    class ReqParser
    {
        public static int PORT = 80;  // http default port

        // create HTTP GET request string
        public static string GetRequestString(string hostname, string endpoint)
        {
            return "GET " + endpoint + " HTTP/1.1\r\n" +
                   "Host: " + hostname + "\r\n" +
                   "Content-Length: 0\r\n\r\n";
        }

        public static int GetContentLen(string responseContent)
        {
            var contentLen = 0;
            var respLines = responseContent.Split('\r', '\n');
            foreach (string respLine in respLines)
            {
                var headDetails = respLine.Split(':');

                if (String.Compare(headDetails[0], "Content-Length", StringComparison.Ordinal) == 0)
                {
                    contentLen = int.Parse(headDetails[1]);
                }
            }
            return contentLen;
        }
        public static bool ResponseHeaderObtained(string responseContent)
        {
            return responseContent.Contains("\r\n\r\n");
        }
    }
}
