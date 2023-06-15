To add a new vertex to a graph, you need to follow these steps:

1.  Create the new vertex by assigning it a unique identifier (e.g., a name or number).
2.  Allocate memory for the new vertex.
3.  Add the new vertex to the vertex set of the graph.
4.  If the graph is undirected, add an entry for the new vertex in the adjacency list or matrix for each existing vertex.
5.  If the graph is directed, add an entry only for the vertices that are adjacent to the new vertex.

For example, suppose you have a graph with vertices A, B, C, and D. To add a new vertex E to the graph, you would create the vertex E, allocate memory for it, add it to the vertex set of the graph, and then update the adjacency matrix or list as follows:

```python
   A  B  C  D  E
A  0  1  1  0  0
B  1  0  0  1  0
C  1  0  0  0  1
D  0  1  0  0  1
E  0  0  1  1  0
```

This matrix represents an undirected graph, where each row and column corresponds to a vertex, and the entries indicate whether the corresponding vertices are adjacent (i.e., connected by an edge). The entry in row E and column C is 1, indicating that vertex E is adjacent to vertex C.


___
Type: #microtopic 
Topics: [[Computer Science]], [[Data Structures]], [[Graph]]

