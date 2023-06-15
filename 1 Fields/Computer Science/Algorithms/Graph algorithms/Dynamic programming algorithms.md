**Dynamic Programming**: Optimization technique in computer programming. It involves solving problems that have overlapping subproblems.
-   **Overlapping Subproblems**: Repeated subproblems in a solution.
-   **Optimal Substructure**: Solution built from optimal subproblem solutions.
-   **Memoization**: Top-down DP approach, caching results.
-   **Tabulation**: Bottom-up DP approach, filling a table.
-   **Efficiency**: Reduces time complexity of recursive algorithms.
-   **Trade-offs**: Space complexity increases for time efficiency.

___

# Top-down Dynamic Programming using Memoization vs Bottom-up using Tabulation

## **Top-down Dynamic Programming (Memoization)**
- **Definition**: A technique that breaks a problem into smaller overlapping subproblems, solving them recursively and caching the results for future use.
- **Process**:
    1. Identify overlapping subproblems
    2. Create a memoization table to store results
    3. Write a recursive function to solve subproblems
    4. Utilize cached results to avoid redundant calculations
- **Example**: Fibonacci series
    - **Code** (Python):
        ```python
        def fib_memo(n, memo):
            if memo[n] is not None:
                return memo[n]
            if n <= 2:
                result = 1
            else:
                result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
            memo[n] = result
            return result

        def fib(n):
            memo = [None] * (n + 1)
            return fib_memo(n, memo)
        ```
- **Strengths**:
    - **Intuitive**: Reflects natural problem-solving approach.
    - **Efficient**: Reuses cached results to reduce redundant calculations.
- **Weaknesses**:
    - **Overhead**: Recursive calls and memoization may increase memory usage and runtime.

## **Bottom-up Dynamic Programming (Tabulation)**
- **Definition**: A technique that solves a problem iteratively by building a table of results from smaller to larger subproblems.
- **Process**:
    1. Identify overlapping subproblems
    2. Create a table to store results
    3. Iterate through subproblems to build the table
    4. Access the final result from the table
- **Example**: Fibonacci series
    - **Code** (Python):
        ```python
        def fib(n):
            if n <= 2:
                return 1
            fib_table = [0, 1, 1]
            for i in range(3, n + 1):
                fib_table.append(fib_table[-1] + fib_table[-2])
            return fib_table[n]
        ```
- **Strengths**:
    - **Optimized**: Minimizes runtime and memory usage.
    - **Scalable**: Better suited for large-scale problems.
- **Weaknesses**:
    - **Less intuitive**: May require rethinking problem-solving approach.

## **Comparison**
- **Similarities**:
    - Both techniques address overlapping subproblems.
    - Both use data structures (memoization table or table) to store results.
- **Differences**:
    - **Approach**: Top-down uses recursion, while bottom-up uses iteration.
    - **Memory usage**: Top-down may have higher memory usage due to recursive calls and memoization, while bottom-up uses a single table.
    - **Intuitiveness**: Top-down is more intuitive but may be less efficient, while bottom-up is less intuitive but more efficient.

___
### Tip for self
Dynamic programming problems are usually solvable by implementing a recursive solution then adding memoization (store computational results in a dictionary):

1. Base case
2. Recursive case
3. Add memoization (the variables that should be memoized are the variables that change with recursive calls)

___
Topics: [[Computer Science]], [[Algorithms]], [[Graph algorithms]]
Type: #microtopic 
