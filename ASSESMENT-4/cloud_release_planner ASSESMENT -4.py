"""
Cloud Release Budget Planner  (CSA06 - CO4 Coding Challenge)

Reads from standard input:
    n W
    <name> <cost> <value>      (n lines)

Prints exactly four lines:
    Greedy Value = G
    Maximum Value = V
    Selected = <names in input order separated by single spaces, or NONE>
    Budget Used = B

Algorithms
    Greedy : sort by value/cost (decreasing), take a feature if it still fits.
    DP     : 0/1 knapsack, O(n * W) time, O(W) values + n*(W+1) decision bytes.
    Tie    : among selections with maximum value, the smallest budget is reported.
"""
import sys
from functools import cmp_to_key


def greedy_value(budget, items):
    """Value obtained by the 'value per unit cost' rule.

    items = list of (name, cost, value).
    Features are ordered by decreasing value/cost (compared exactly with
    cross-multiplication, equal ratios keep input order); a feature is taken
    whenever it still fits in the remaining budget.
    """
    def cmp(i, j):
        # i before j  <=>  value_i / cost_i > value_j / cost_j
        return items[j][2] * items[i][1] - items[i][2] * items[j][1]

    order = sorted(range(len(items)), key=cmp_to_key(cmp))
    used = total = 0
    for i in order:
        _, cost, value = items[i]
        if used + cost <= budget:
            used += cost
            total += value
    return total


def knapsack(budget, items):
    """Optimal plan. Returns (max_value, budget_used, chosen_indices)."""
    n = len(items)
    # best[w] = maximum value using the features processed so far with total cost <= w
    best = [0] * (budget + 1)
    # taken[i][w] = 1 when feature i is used in the optimum for capacity w (row i)
    taken = []
    for _, cost, value in items:
        flags = bytearray(budget + 1)
        if cost <= budget:
            head = best[:cost]                                   # w < cost : cannot take
            tail = best[cost:]                                   # w >= cost: skip value
            cand = [b + value for b in best[:budget - cost + 1]]  # take value: best[w-cost] + value
            flags[cost:] = bytearray(c > s for s, c in zip(tail, cand))  # strict: ties -> skip
            best = head + [s if s >= c else c for s, c in zip(tail, cand)]
        taken.append(flags)

    max_value = best[budget]
    # best[] is non-decreasing in w, so the first capacity that reaches the
    # maximum is the smallest budget needed by any optimal selection.
    budget_used = best.index(max_value)

    chosen = []
    w = budget_used
    for i in range(n - 1, -1, -1):
        if taken[i][w]:
            chosen.append(i)
            w -= items[i][1]
    chosen.reverse()
    return max_value, budget_used, chosen


def solve(budget, items):
    """Return the four output lines as a list of strings."""
    g = greedy_value(budget, items)
    v, b, chosen = knapsack(budget, items)
    names = " ".join(items[i][0] for i in chosen) if chosen else "NONE"
    return [f"Greedy Value = {g}", f"Maximum Value = {v}",
            f"Selected = {names}", f"Budget Used = {b}"]


def main():
    tokens = sys.stdin.read().split()
    n, budget = int(tokens[0]), int(tokens[1])
    items = []
    pos = 2
    for _ in range(n):
        items.append((tokens[pos], int(tokens[pos + 1]), int(tokens[pos + 2])))
        pos += 3
    print("\n".join(solve(budget, items)))


if __name__ == "__main__":
    main()
