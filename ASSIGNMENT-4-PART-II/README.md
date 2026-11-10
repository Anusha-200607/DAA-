# DAA Assignment 4 – Part II: Algorithm Engineering (CO4)

## Student Details

- **Name:** ANUSHA BHASKAR
- **Register Number:** 1924016
- **Course:** Design and Analysis of Algorithms (CSA0610)
- **Mode:** Individual
- **Programming Language:** Python 3

---

## 1. Assignment Overview

This assignment focuses on implementing, testing, analysing, and improving algorithms using Python 3. It covers dynamic programming, greedy algorithms, graph algorithms, minimum spanning trees, and optimisation problems.

The main objective is to understand how algorithmic design decisions affect correctness, execution time, memory usage, and solution quality under different requirements.

## 2. Tasks Covered

### Task 1 – Word Wrap Using Dynamic Programming

**Algorithm:** Dynamic Programming

- Finds the minimum total penalty when arranging words within a fixed line width.
- Uses suffix-based DP states.
- Applies squared unused spaces as the line penalty.
- Keeps the final line penalty as zero.
- Handles exact-fit words, empty text, single-word input, and words longer than the available width.
- Tests different widths: 20, 30, 40, and 60.

**Result:** For width 30, the minimum total penalty is **57**.

### Task 2 – Greedy Versus Dynamic Programming

**Algorithms:**
- Fractional Knapsack using Greedy.
- 0/1 Knapsack using Greedy.
- 0/1 Knapsack using Dynamic Programming.

This task compares greedy and DP solutions based on:
- Value-to-weight ratios.
- Item selection.
- Execution operation counts.
- Memory requirements.
- Solution quality.
- Random and adversarial test cases.

**Key Finding:** Greedy is optimal for the fractional knapsack problem but does not guarantee an optimal solution for 0/1 knapsack. Dynamic Programming provides an exact solution for 0/1 knapsack.

A safeguarded greedy approach is also evaluated for situations where speed is more important than exact optimality.

### Task 3 – Routing Engine

**Algorithms:**
- Dijkstra's Algorithm.
- Bellman-Ford Algorithm.
- Floyd-Warshall Algorithm.
- Warshall's Algorithm.

This task implements shortest-path and reachability algorithms on a directed graph.

It evaluates:
- Shortest paths from a source vertex.
- The effect of negative-weight edges.
- Negative-cycle detection.
- All-pairs shortest paths.
- Graph reachability.

**Key Finding:** Dijkstra's Algorithm is not suitable for graphs containing negative-weight edges. Bellman-Ford can handle negative edges and detect reachable negative cycles.

### Task 4 – Assembly Line Scheduling

**Algorithm:** Dynamic Programming

This task calculates the minimum production time across two assembly lines.

It considers:
- Station processing times.
- Entry and exit times.
- Transfer times between lines.
- Route reconstruction.
- Changes in production conditions.
- Extension to three assembly lines.

**Result:** The minimum production time for the base case is **38**.

The implementation is also validated against exhaustive enumeration on 300 random instances.

### Task 5 – Kruskal, Prim, and Borůvka Algorithms

**Algorithms:**
- Kruskal's Algorithm.
- Prim's Algorithm.
- Borůvka's Algorithm.

This task compares three Minimum Spanning Tree (MST) algorithms.

It covers:
- Safe edge selection.
- Union-Find data structures.
- Priority queues.
- Component merging.
- Equal-weight edge handling.
- Sparse and dense graph analysis.
- Distributed and parallel processing considerations.

**Result:** All three algorithms produce an MST with a total cost of **35** for the given graph.

### Task 6 – Last-Mile Delivery Using TSP Dynamic Programming

**Algorithm:** Travelling Salesperson Problem using Dynamic Programming (Held-Karp approach).

This task develops an optimisation solution for a delivery routing system.

It includes:
- Problem modelling.
- Bitmask-based DP states.
- State transitions.
- Route reconstruction.
- Comparison with brute-force enumeration.
- State-space growth analysis.
- Evaluation of heuristic approaches for larger inputs.

**Result:** The optimal delivery route is:

`Hub → D → C → A → E → F → B → Hub`

**Minimum Travel Cost:** 69

The implementation is validated against brute force on 300 random asymmetric instances.

---

## 3. Algorithms and Concepts Used

| Task | Main Algorithm | Important Concepts |
|---|---|---|
| Task 1 | Dynamic Programming | Word Wrap, Recurrence, State Reconstruction |
| Task 2 | Greedy and Dynamic Programming | Fractional Knapsack, 0/1 Knapsack |
| Task 3 | Graph Algorithms | Dijkstra, Bellman-Ford, Floyd-Warshall, Warshall |
| Task 4 | Dynamic Programming | Assembly Line Scheduling |
| Task 5 | Minimum Spanning Tree | Kruskal, Prim, Borůvka, Union-Find |
| Task 6 | Dynamic Programming | Travelling Salesperson Problem, Bitmask DP |

## 4. Project Files

The repository contains the following files:

```text
DAA-Assignment-4-Part-II-CO4/
│
├── README.md
├── daa_4b.py
├── daa_4b_output.txt
└── DAA_Assignment_4_Part_II_CO4.docx
```

**File Description:**

- `README.md` – Assignment overview, algorithms, and execution instructions.
- `daa_4b.py` – Python source code containing one function per algorithm and separate `task1()` to `task6()` printing functions.
- `daa_4b_output.txt` – Complete raw program output.
- `DAA_Assignment_4_Part_II_CO4.docx` – Assignment report and explanations.

## 5. Requirements

- Python 3
- Any Python-compatible operating system.
- Command Prompt, Terminal, or VS Code.

No additional Python packages are specified as requirements for running the program.

## 6. How to Execute

### Step 1: Open the Project Folder

Open the assignment folder in Command Prompt or Terminal.

### Step 2: Run the Python Program

Execute:

```bash
python3 daa_4b.py
```

On Windows, if `python3` is not recognised, use:

```bash
python daa_4b.py
```

### Step 3: Verify the Output

The program executes all six tasks and displays their results.

Compare the generated results with:

`daa_4b_output.txt`

## 7. Testing and Validation

The assignment includes several testing and validation methods:

- Word Wrap boundary testing and width changes.
- Greedy versus DP comparison on 3,000 random knapsack instances.
- Shortest-path comparison between Dijkstra and Bellman-Ford.
- Negative-cycle detection.
- Floyd-Warshall and Warshall matrix verification.
- Assembly Line Scheduling validation on 300 random instances.
- MST comparison using Kruskal, Prim, and Borůvka.
- TSP validation against brute force on 300 random instances.
- Boundary testing for empty and single-location TSP inputs.

## 8. Key Learning Outcomes

Through this assignment, the following concepts were studied and implemented:

1. Designing and implementing dynamic programming algorithms.
2. Comparing greedy and dynamic programming approaches.
3. Understanding shortest-path algorithms and negative-weight edges.
4. Detecting negative cycles in directed graphs.
5. Implementing assembly line scheduling.
6. Understanding Minimum Spanning Tree algorithms.
7. Analysing time and space complexity.
8. Performing boundary testing and validation.
9. Comparing algorithm performance using operation counts.
10. Understanding the limitations of exact algorithms for large optimisation problems.

## 9. Conclusion

DAA Assignment 4 – Part II demonstrates the practical application of algorithm engineering using Python 3. The six tasks explore dynamic programming, greedy methods, graph algorithms, scheduling, minimum spanning trees, and travelling salesperson optimisation.

The implementations are supported by execution outputs, boundary tests, random-instance validation, and performance analysis. The assignment highlights the importance of selecting appropriate algorithms based on correctness, efficiency, memory requirements, and real-world constraints.

---

**Submitted by:** ANUSHA BHASKAR  
**Register Number:** 1924016  
**Course:** Design and Analysis of Algorithms (CSA0610)  
**Date:** 10/11/2026
