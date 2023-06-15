Dijkstra's algorithm is a shortest-path algorithm that finds the shortest path between a source vertex and all other vertices in a weighted graph. The algorithm works by maintaining a priority queue of vertices to be processed, where the priority of a vertex is determined by its distance from the source vertex.

## Algorithm

The steps of the Dijkstra's algorithm are as follows:

1.  Initialize a distance table with the source vertex having a distance of 0 and all other vertices having a distance of infinity.
2.  Add the source vertex to a priority queue and set its distance as 0.
3.  Repeat the following until the priority queue is empty: a. Dequeue the vertex with the smallest distance from the priority queue. b. For each neighbor of the dequeued vertex, calculate the distance from the source vertex through this vertex and update the distance in the distance table if it's smaller. c. Add the neighbors of the dequeued vertex to the priority queue.
4.  The final distance table contains the shortest distance from the source vertex to all other vertices.

## Implementation

Here's an example of Dijkstra's algorithm implementation in Python:
```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        (current_distance, current_vertex) = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}
print(dijkstra(graph, 'A')) # Output: {'A': 0, 'B': 1, 'C': 2, 'D': 3}

```

## Explanation

The input graph is represented as a dictionary where the keys are the vertices and the values are dictionaries of the form `{neighbor: weight}` representing the edges and their weights.

In the algorithm, the distance table is initialized with the source vertex having a distance of 0 and all other vertices having a distance of infinity. The priority queue is initialized with the source vertex and its distance.

The algorithm then repeatedly dequeues the vertex with the smallest distance from the priority queue and updates the distances of its neighbors if necessary. The neighbors are then added to the priority queue.

The final distance table contains the shortest distances from the source vertex to all other vertices.


___
Type: #microtopic 
Topics: [[Computer Science]], [[Algorithms]], [[Search algorithms]]

