/**
 * Program that is capable of simultaneously downloading several files through HTTP. 
 * Socket functions used: BeginConnect()/EndConnect(), BeginSend()/EndSend() and BeginReceive()/EndReceive(). 
 * The "ReqParser" class is a simple parser for the HTTP protocol (it gets the header lines and understands the Content-lenght: header line).
 */


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FuturesContinuations.Implementation;

namespace FuturesContinuations
{
    class Program
    {
        static void Main(string[] args)
        {
            var hosts = new string[] { "www.cs.ubbcluj.ro/~rlupsa/edu/pdp/lecture-2-handling-concurrency.html",
                                       "www.cs.ubbcluj.ro/~rlupsa/edu/pdp/lecture-5-futures-continuations.html",
                                       "www.cs.ubbcluj.ro/~rlupsa/edu/pdp/lecture-7-parallel-simple.html" }.ToList();

            //CallbackImpl.run(hosts);
            //TaskImpl.run(hosts);
            TaskAsyncImpl.run(hosts);

        }
    }
}
