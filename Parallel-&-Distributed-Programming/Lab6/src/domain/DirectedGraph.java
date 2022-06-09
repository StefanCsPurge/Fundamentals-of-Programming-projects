package domain;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static java.util.Collections.shuffle;

public class DirectedGraph {
    List<Integer> nodes;
    List<List<Integer>> nextNeighbors;

    public DirectedGraph(int noOfNodes) {
        this.nodes = new ArrayList<>();
        this.nextNeighbors = new ArrayList<>();

        for(int i=0;i<noOfNodes; i++){
            this.nodes.add(i);
            this.nextNeighbors.add(new ArrayList<>());
        }
    }

    public List<Integer> getNodes(){
        return nodes;
    }

    public List<Integer> getNextNeighborsOf(int node){
        if(node < 0 || node >= nodes.size())
            return new ArrayList<>();
        return this.nextNeighbors.get(node);
    }

    public void addEdge(int nodeA, int nodeB) {
        this.nextNeighbors.get(nodeA).add(nodeB);
    }

    public static DirectedGraph generateHamiltonianDG(int noOfNodes) {
        DirectedGraph graph = new DirectedGraph(noOfNodes);
        var nodes = graph.getNodes();
        shuffle(nodes);

        for (int i=1; i<noOfNodes; i++)
            graph.addEdge(nodes.get(i - 1),  nodes.get(i));
        graph.addEdge(nodes.get(noOfNodes-1), nodes.get(0));  // close cycle

        Random random = new Random();

        for (int i = 0; i < noOfNodes / 3; i++){      // add some more random edges
            int nodeA = random.nextInt(noOfNodes);
            int nodeB = random.nextInt(noOfNodes);
            graph.addEdge(nodeA, nodeB);
        }
        return graph;
    }



}
