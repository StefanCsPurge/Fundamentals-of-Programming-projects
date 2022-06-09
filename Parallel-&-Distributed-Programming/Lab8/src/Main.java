import mpi.MPI;
import msg.CloseMessage;
import msg.Message;
import msg.SubscribeMessage;
import msg.UpdateMessage;

/**
 A simple distributed shared memory (DSM) mechanism. A main program and a DSM library are implemented.
 There is a predefined number of communicating processes.
 The DSM mechanism provides a predefined number of integer variables residing on each of the processes.

 The DSM provides the following operations:
 - write a value to a variable (local or residing in another process);
 - a callback informing the main program that a variable managed by the DSM has changed.
   All processes receive the same sequence of data change callbacks;
   it is not allowed that process P sees first a change on a variable A and then a change on a variable B, while another process Q sees the change on B first and the change on A second.
 - a "compare and exchange" operation, that compares a variable with a given value and, if equal, it sets the variable to another given value.
   The interaction with the previous operation is taken into consideration.
*/

public class Main {

    public static void main(String[] args) throws InterruptedException {
        MPI.Init(args);
        DSM dsm = new DSM();
        int me = MPI.COMM_WORLD.Rank();
        if (me == 0) {
            Thread thread = new Thread(new Listener(dsm));
            thread.start();

            dsm.subscribeTo("a");
            dsm.subscribeTo("b");
            dsm.subscribeTo("c");
            dsm.checkAndReplace("a",0,222);
            dsm.checkAndReplace("c",2,555);
            dsm.checkAndReplace("b",100, 401);
            dsm.close();

            thread.join();

        } else if (me == 1) {
            Thread thread = new Thread(new Listener(dsm));
            thread.start();

            dsm.subscribeTo("a");
            dsm.subscribeTo("c");

            thread.join();
        } else if (me == 2) {
            Thread thread = new Thread(new Listener(dsm));

            thread.start();

            dsm.subscribeTo("b");
            dsm.checkAndReplace("b", 1, 99);

            thread.join();
        }
        MPI.Finalize();
    }

    private record Listener(DSM dsm) implements Runnable {

        @Override
        public void run() {
            while (true) {
                System.out.println("Process " + MPI.COMM_WORLD.Rank() + " waiting..");
                Object[] messages = new Object[1];

                MPI.COMM_WORLD.Recv(messages, 0, 1, MPI.OBJECT, MPI.ANY_SOURCE, MPI.ANY_TAG);
                Message message = (Message) messages[0];

                if (message instanceof CloseMessage) {
                    System.out.println("Process " + MPI.COMM_WORLD.Rank() + " stopped listening...");
                    return;
                } else if (message instanceof SubscribeMessage subscribeMessage) {
                    System.out.println("Subscribe message received");
                    System.out.println("Process " + MPI.COMM_WORLD.Rank() + " received: process " + subscribeMessage.rank + " subscribes to " + subscribeMessage.var);
                    dsm.syncSubscription(subscribeMessage.var, subscribeMessage.rank);
                } else if (message instanceof UpdateMessage updateMessage) {
                    System.out.println("Update message received");
                    System.out.println("Process " + MPI.COMM_WORLD.Rank() + " received:" + updateMessage.var + "->" + updateMessage.val);
                    dsm.setVariable(updateMessage.var, updateMessage.val);
                }

                writeAll(dsm);
            }
        }
    }

    public static void writeAll(DSM dsm) {
        StringBuilder sb = new StringBuilder();
        sb.append("\nWrite all\n");
        sb.append("Process ").append(MPI.COMM_WORLD.Rank()).append(" -> a = ").append(dsm.a).append("  b = ").append(dsm.b).append("  c = ").append(dsm.c).append("\n");
        sb.append("Subscribers: \n");
        for (String var : dsm.subscribers.keySet()) {
            sb.append(var).append(" -> ").append(dsm.subscribers.get(var).toString()).append("\n");
        }
        System.out.println(sb);
    }

}
