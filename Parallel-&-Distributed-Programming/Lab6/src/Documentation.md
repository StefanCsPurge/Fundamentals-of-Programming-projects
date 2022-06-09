# Parallelizing techniques (2 - parallel explore) for finding Hamiltonian cycles in directed graphs

Algorithm
---------
- each node of the graph is taken into consideration as a starting point for the search
- the process goes through the next neighbours of the current node, while updating the current path (backtracking)
- this recursive search stops when the path contains all the nodes of the directed graph

Synchronization
---------------
- a Java ReentrantLock is used to protect the result (list of nodes)
- the AtomicBoolean variable is used to stop all the threads when a cycle is found

Performance measurements
------------------------
- number of threads set to: 5
- time measurement unit: ms

| Number of nodes | Time |
|-----------------|------|
|10 | 15 |
|100 | 13 |
|222 | 21 |
|600 | 68 |
|999 | 45 |
|2000| 117 |


