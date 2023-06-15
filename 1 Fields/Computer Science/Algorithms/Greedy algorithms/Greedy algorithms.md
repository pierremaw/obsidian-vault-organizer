**Greedy algorithms**: make locally optimal choices at each step, aiming for a globally optimal solution
    * **Characteristics**: Simple, fast, easy to implement
    * **Drawbacks**: May not always produce the optimal solution

* **Examples of Greedy Algorithms**
    * **Dijkstra's Algorithm**: Shortest path in a weighted graph
    * **Kruskal's Algorithm**: Minimum spanning tree in a connected, undirected graph
    * **Prim's Algorithm**: Another minimum spanning tree algorithm
    * **Huffman Coding**: Lossless data compression
    * **Fractional Knapsack Problem**: Maximizing the value of items picked, considering fractional amounts

* **Greedy Algorithm Components**
    * **Candidate Set**: Set of possible solutions to choose from
    * **Selection Function**: Criteria for choosing the best candidate
    * **Feasibility Function**: Determines if a candidate can be part of a solution
    * **Objective Function**: Evaluates the quality of a solution
    * **Solution Function**: Determines when a solution is complete

* **Greedy Algorithm Steps**
    1. **Initialize**: Start with an empty solution
    2. **Select**: Choose the best candidate from the candidate set, based on the selection function
    3. **Evaluate**: Check if the chosen candidate is feasible using the feasibility function
    4. **Update**: If feasible, update the solution and candidate set
    5. **Terminate**: Repeat steps 2-4 until the solution function indicates completion or no more candidates

* **When to Use Greedy Algorithms**
    * **Optimal Substructure**: Optimal solution can be constructed from optimal solutions of subproblems
    * **Greedy Choice Property**: Locally optimal choices lead to a globally optimal solution
    * **No Backtracking**: The algorithm does not need to undo its choices


___
Type: #subtopic 
Topics: [[Computer Science]], [[Algorithms]]

