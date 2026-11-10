# CSA06 – CO4 Coding Challenge: Cloud Release Budget Planner

**Course:** CSA06 – Design and Analysis of Algorithms
**Assessment:** CO4 – Assessment Tool 1: Coding Challenge (Individual, in class)
**Student:** Anusha  |  **Reg. No.:** 192465016
**Language:** Python 3 (standard library only)

## Problem

A SaaS company has `n` candidate features. Feature `i` costs `cost[i]` units of the monthly cloud budget and delivers `value[i]`. Each feature is deployed completely or not at all, and the total cost must not exceed the budget `W`. The program chooses the features that maximise total value (0/1 knapsack) and also reports what the greedy "value per unit cost" rule would have achieved.

Constraints: `1 ≤ n ≤ 200`, `0 ≤ W ≤ 10,000`, `1 ≤ cost ≤ 1,000`, `0 ≤ value ≤ 1,000`, time limit 2 seconds.

## Repository contents

| File | Description |
|------|-------------|
| `cloud_release_planner.py` | The solution: greedy rule, dynamic programming, plan reconstruction. Reads standard input |
| `test_planner.py` | Tests: both samples, edge cases, a brute-force cross-check and a maximum-size test |
| `CSA06_CO4_Coding_Challenge_Anusha.docx` | Written report for tasks (a) to (d) |
| `README.md` | This file |

## Input and output

Input:

```
n W
<name> <cost> <value>      (n lines)
```

Output (exactly four lines):

```
Greedy Value = G
Maximum Value = V
Selected = <names in input order separated by single spaces, or NONE>
Budget Used = B
```

If several selections give the maximum value, the one with the smallest `Budget Used` is reported.

## How to run

```bash
# run the solution
python cloud_release_planner.py < input.txt

# or type the input directly
printf '3 50\nAuth 10 60\nSearch 20 100\nPayments 30 120\n' | python cloud_release_planner.py

# run all tests
python test_planner.py
```

Sample 1 output:

```
Greedy Value = 160
Maximum Value = 220
Selected = Search Payments
Budget Used = 50
```

## Approach

- **Greedy (task a):** sort features by decreasing value/cost (ratios compared exactly by cross-multiplication, ties keep input order) and take a feature whenever it still fits; a feature that does not fit is skipped and the scan continues. On Sample 1 it gets 160 against the optimum 220.
- **Dynamic programming (task b):** `f(i, w)` is the best value using the first `i` features with total cost at most `w`. `f(0, w) = 0`, `f(i, 0) = 0`, and `f(i, w) = max(f(i-1, w), f(i-1, w - cost_i) + value_i)` when `cost_i ≤ w`, otherwise `f(i-1, w)`. Rows are filled for `i = 1..n`; the code keeps one value array and builds each new row from the old one, so no feature is used twice.
- **Reconstruction (task c):** `Budget Used` is the smallest capacity `w` where `f(n, w)` already equals the maximum, which implements the tie-breaking rule. A decision table `taken[i][w]` is walked back from `i = n` to rebuild the plan, which is printed in input order (`NONE` when nothing is selected).
- **Analysis (task d):** time `Θ(n·W)` (about 2 × 10⁶ cell updates at the maximum), space `O(n·W)` bytes for the decision table (about 2 MB). The DP is pseudo-polynomial: `W` is written with `log2 W` bits, so `n·W` is exponential in the input length.

## Test summary

`python test_planner.py` checks:

- Sample 1 and Sample 2 (exact output text, through the command line)
- Zero budget, no service fits, every service fits, tied optima, single service (fits and too costly), a zero-value service, and a case where greedy fails
- 3,000 random small inputs against a brute-force search (value, smallest budget and the selected plan)
- A random input at the maximum size (`n = 200`, `W = 10,000`): about 0.2 s for the whole program, and the maximum value matches an independent plain DP

## Notes

- The greedy rule is implemented as "take a feature if it still fits, otherwise skip it and continue". Both samples give the expected Greedy Value (160 and 146) under this reading.
- Features with value 0 are never selected, because they would only increase the budget used.
