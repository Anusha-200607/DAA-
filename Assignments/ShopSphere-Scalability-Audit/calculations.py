"""Selected numeric checks for the ShopSphere DAA assignment.
Run with: python calculations.py
"""
from math import ceil, log2

OPS_PER_SECOND = 10**8
N = 1_000_000

m1 = N * (N - 1) // 2
m2 = 2 ** ceil(log2(N)) - 1
binary_search_comparisons = ceil(log2(N))

print(f"M1 comparisons: {m1:,}")
print(f"M1 time: {m1 / OPS_PER_SECOND:.3f} seconds")
print(f"M2 audit operations: {m2:,}")
print(f"M2 time: {m2 / OPS_PER_SECOND:.6f} seconds")
print(f"S2 worst-case comparison estimate: {binary_search_comparisons}")
print(f"S2 time per search: {binary_search_comparisons / OPS_PER_SECOND:.10f} seconds")

# Recurrence estimates assume T(1)=1 and use k ~= log2(N).
k = log2(N)
m4_current = 2 * N**2 - N
m4_redesign = N * k + N
m5 = N * (1 + k * (k + 1) / 2)

print(f"M4 current estimated operations: {m4_current:,.0f}")
print(f"M4 current estimated time: {m4_current / OPS_PER_SECOND:.3f} seconds")
print(f"M4 redesign estimated operations: {m4_redesign:,.0f}")
print(f"M4 redesign estimated time: {m4_redesign / OPS_PER_SECOND:.6f} seconds")
print(f"M5 estimated operations: {m5:,.0f}")
print(f"M5 estimated time: {m5 / OPS_PER_SECOND:.6f} seconds")
