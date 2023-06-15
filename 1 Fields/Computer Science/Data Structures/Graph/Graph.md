* **A graph** is a data structure where vertices are connected using edges. A graph can represent relationships between objects
    * **Components**: Vertices (nodes) and edges (connections)
    * **Use Cases**: Social networks, transportation networks, web pages, dependencies, etc.

* **Types of Graphs**
    * **Undirected Graph**: Edges have no direction, indicating a mutual relationship
    * **Directed Graph (Digraph)**: Edges have a direction, indicating a one-way relationship
    * **Weighted Graph**: Edges have associated weights, representing the cost or strength of the connection
    * **Unweighted Graph**: Edges have no weights, representing equal cost or strength for all connections
    * **Cyclic Graph**: Contains at least one cycle (a cycle is a path that starts and ends on the same vertex)
    * **Acyclic Graph**: Contains no cycles
    * **Connected Graph**: There exists a path between any two vertices
    * **Disconnected Graph**: Not all vertices are reachable from each other

* **Graph Representations**
    * **Adjacency Matrix**: Square matrix with rows and columns representing vertices; cell values indicate edge presence or weight
        * **Pros**: Constant-time access to check if an edge exists; easy to implement
        * **Cons**: Space complexity of O(V^2), even for sparse graphs
    * **Adjacency List**: Array or hashmap where each entry corresponds to a vertex and stores a list of its adjacent vertices
        * **Pros**: Space complexity of O(V + E); efficient for sparse graphs
        * **Cons**: Checking for edge existence may take longer than with an adjacency matrix

* **Graph Traversal Algorithms**: used to explore all vertices, one vertex at a time.
    * **Depth-First Search (DFS)**: Explore as far as possible along each branch before backtracking
        * **Applications**: Pathfinding, cycle detection, topological sorting, etc.
    * **Breadth-First Search (BFS)**: Explore all neighbors at the current depth before moving to nodes at the next depth level
        * **Applications**: Shortest path (unweighted graphs), connected components, bipartite checking, etc.

* **Graph Algorithms**
    * **Shortest Path Algorithms**: Dijkstra, Bellman-Ford, A*
    * **Minimum Spanning Tree Algorithms**: Kruskal, Prim
    * **Connectivity Algorithms**: Kosaraju, Tarjan
    * **Flow Algorithms**: Ford-Fulkerson, Edmonds-Karp, Dinic
    * **Matching Algorithms**: Hungarian, Hopcroft-Karp
    * **Centrality Measures**: Degree, closeness, betweenness, eigenvector
    * **Clustering Algorithms**: Girvan-Newman, Louvain, spectral clustering

___
Topics: [[Computer Science]], [[Data Structures]]
Type: #subtopic 

