- **Depth First Search (DFS)**: An algorithm for traversing or searching graph data structures.
  - **Traversal**: Visiting each node in a graph or tree in a specific order.
  - **Search**: Finding a specific node or path in a graph or tree.

- **Algorithm**: DFS explores as far as possible along each branch before backtracking.
  1. **Start**: Select a starting node.
  2. **Visit**: Mark the current node as visited.
  3. **Explore**: Visit all unvisited adjacent nodes.
  4. **Backtrack**: If no unvisited adjacent nodes, backtrack to the previous node and repeat step 3.
  5. **Termination**: When all nodes are visited or the desired node is found.

- **Implementation**: DFS can be implemented using recursion or an explicit stack data structure.
  - **Recursive**: A function calls itself for each unvisited adjacent node.
  - **Iterative**: An explicit stack is used to manage the traversal process.

- **Applications**: DFS has several use cases in computer science.
  - **Cycle Detection**: Determine if a graph contains a cycle.
  - **Pathfinding**: Find a path between two nodes in a graph.
  - **Topological Sorting**: Sort nodes in a directed acyclic graph (DAG) by their dependencies.
  - **Maze Solving**: Solve a maze by finding a path from the entrance to the exit.

- **Complexity**: The time and space complexity of DFS is O(V + E), where V is the number of vertices and E is the number of edges.
  - **Time Complexity**: Each node and edge is visited once.
  - **Space Complexity**: The maximum depth of the stack or recursion can be equal to the number of vertices.

- **Advantages**:
  - **Simplicity**: DFS is relatively easy to implement.
  - **Low Memory Overhead**: DFS uses less memory than other search algorithms like Breadth First Search.

- **Disadvantages**:
  - **Non-optimal Solutions**: DFS might find a non-optimal solution in some cases, such as pathfinding.
  - **Infinite Loops**: DFS may get stuck in an infinite loop if the graph contains a cycle and cycle detection is not implemented.

___

### Recursive DFS
```
def dfs_recursive(graph, node, visited):
	# Mark the node as visited
    visited.add(node)
	
	# Process the code
	do_something(node)

	# Recursively visit the unvisited neighbours
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

############################################################

# Usage example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
dfs_recursive(graph, 'A', visited)
```

### Iterative DFS

```
def dfs_iterative(graph, start):
	# Initialize an empty stack and a visited set
    visited = set()
    stack = []

	# Push the source node to the stack
	stack.append(start)

	# Loop until the stack is empty
    while stack:
	    # Pop a node from the stack
        node = stack.pop()

		# If the node has not been visited
        if node not in visited:

			# Mark it as visited
			visited.add(node)

			# Process the node
			do_something(node)

			# Push its unvisited neighbours onto the stack
			for neighbour in graph[node]:
				if neighbour not in visited:
					stack.append(neighbour) 			
			
############################################################

# Usage example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_iterative(graph, 'A')

```

___
Type: #microtopic 
Topics: [[Computer Science]], [[Algorithms]], [[Search algorithms]]

