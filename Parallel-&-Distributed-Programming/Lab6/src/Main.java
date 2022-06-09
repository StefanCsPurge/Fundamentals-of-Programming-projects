import domain.DirectedGraph;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Given a directed graph, find a Hamiltonian cycle, if one exists.
 * Multiple threads are used to parallelize the search.
 */

public class Main {
    static List<Integer> result = new ArrayList<>();
    static DirectedGraph graph = DirectedGraph.generateHamiltonianDG(2000);
    static AtomicBoolean found = new AtomicBoolean(false);
    static Lock lock = new ReentrantLock();      // https://www.baeldung.com/java-binary-semaphore-vs-reentrant-lock

    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        new Main().findHamiltonianCycleThreaded(graph);
        long end = System.currentTimeMillis();
        System.out.println("Threaded Hamiltonian cycle search: ");
        System.out.println("- execution time: " + (end - start) + " ms");
        System.out.println("- result: " + result + "\n");
    }

    private void findHamiltonianCycleThreaded(DirectedGraph graph){
        ExecutorService executor = Executors.newFixedThreadPool(5);

        for(int i=0; i < graph.getNodes().size(); i++){
            int startingNode = i;   // threads take different starting nodes
            executor.submit(() -> search(startingNode, startingNode, new ArrayList<>()));
        }

        executor.shutdown();
        try {
            var r = executor.awaitTermination(22, TimeUnit.SECONDS);
            if (!r) System.out.println("Threads did not finish.");
        }
        catch (InterruptedException ignored){}
    }

    private void search(int currentNode, int startingNode, List<Integer> path) {
        path.add(currentNode);
        if (found.get()) return;
        if (path.size() == graph.getNodes().size()) {
            if (graph.getNextNeighborsOf(currentNode).contains(startingNode)){
                // found a Hamiltonian cycle
                found.set(true);
                lock.lock();           // protect the shared resource
                result.clear();
                result.addAll(path);
                lock.unlock();
            }
            return;
        }
        graph.getNextNeighborsOf(currentNode).forEach(neighbor -> {
            if (!path.contains(neighbor))
                search(neighbor, startingNode, path);
        });
    }

}
