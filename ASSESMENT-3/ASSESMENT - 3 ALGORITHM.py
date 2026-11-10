"""
KartIQ - Divide-and-Conquer Engine (CSA06 CO3 Case Study)

Implements and verifies the four modules:
  Module 1  Stable Merge Sort (with comparison counter and merge trace)
  Module 2  Quick Sort (Lomuto partition, first-element and median-of-three pivots)
  Module 3  Binary Search (exact and first-occurrence / lower bound)
  Module 4  Strassen matrix multiplication (2x2 verification + hybrid)

Run:  python kartiq_algorithms.py
"""
import math
import random


# --------------------------------------------------------------------------
# Module 1 - Stable Merge Sort
# --------------------------------------------------------------------------
def merge_sort(a, key=lambda x: x, trace=None, counter=None):
    """Return a new stably sorted list. counter[0] accumulates comparisons."""
    if counter is None:
        counter = [0]
    if len(a) <= 1:
        return a[:]
    mid = (len(a) + 1) // 2                               # left half = ceil(n/2), same as mid=(lo+hi)//2
    left = merge_sort(a[:mid], key, trace, counter)      # DIVIDE + CONQUER
    right = merge_sort(a[mid:], key, trace, counter)
    merged, i, j = [], 0, 0                               # COMBINE
    while i < len(left) and j < len(right):
        counter[0] += 1
        if key(left[i]) <= key(right[j]):                 # '<=' keeps stability
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    if trace is not None:
        trace.append((left, right, merged))
    return merged


# --------------------------------------------------------------------------
# Module 2 - Quick Sort
# --------------------------------------------------------------------------
def lomuto_partition(a, lo, hi, counter):
    """Pivot = a[lo]. Returns final pivot index."""
    pivot = a[lo]
    s = lo
    for j in range(lo + 1, hi + 1):
        counter[0] += 1
        if a[j] < pivot:
            s += 1
            a[s], a[j] = a[j], a[s]
    a[lo], a[s] = a[s], a[lo]
    return s


def median_of_three_to_front(a, lo, hi):
    mid = (lo + hi) // 2
    trio = sorted([(a[lo], lo), (a[mid], mid), (a[hi], hi)])
    med_idx = trio[1][1]
    a[lo], a[med_idx] = a[med_idx], a[lo]


def quick_sort(a, strategy="first", counter=None):
    """Iterative-on-larger-side quick sort (stack depth O(log n))."""
    if counter is None:
        counter = [0]

    def qs(lo, hi):
        while lo < hi:
            if strategy == "median3":
                median_of_three_to_front(a, lo, hi)
            elif strategy == "random":
                r = random.randint(lo, hi)
                a[lo], a[r] = a[r], a[lo]
            p = lomuto_partition(a, lo, hi, counter)
            if p - lo < hi - p:          # recurse on smaller part first
                qs(lo, p - 1)
                lo = p + 1
            else:
                qs(p + 1, hi)
                hi = p - 1

    qs(0, len(a) - 1)
    return a, counter[0]


# --------------------------------------------------------------------------
# Module 3 - Binary Search
# --------------------------------------------------------------------------
def binary_search_first(a, target, key=lambda x: x):
    """Index of FIRST element whose key == target, else -1. <= floor(lg n)+1 steps."""
    lo, hi, ans, steps = 0, len(a) - 1, -1, 0
    while lo <= hi:
        steps += 1
        mid = lo + (hi - lo) // 2
        k = key(a[mid])
        if k == target:
            ans = mid
            hi = mid - 1            # keep searching to the LEFT
        elif k < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans, steps


# --------------------------------------------------------------------------
# Module 4 - Strassen
# --------------------------------------------------------------------------
def strassen_2x2(A, B):
    a11, a12, a21, a22 = A[0][0], A[0][1], A[1][0], A[1][1]
    b11, b12, b21, b22 = B[0][0], B[0][1], B[1][0], B[1][1]
    M1 = (a11 + a22) * (b11 + b22)
    M2 = (a21 + a22) * b11
    M3 = a11 * (b12 - b22)
    M4 = a22 * (b21 - b11)
    M5 = (a11 + a12) * b22
    M6 = (a21 - a11) * (b11 + b12)
    M7 = (a12 - a22) * (b21 + b22)
    C = [[M1 + M4 - M5 + M7, M3 + M5],
         [M2 + M4, M1 - M2 + M3 + M6]]
    return C, (M1, M2, M3, M4, M5, M6, M7)


def mat_add(X, Y):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(X, Y)]


def mat_sub(X, Y):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(X, Y)]


def conventional(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def split(M):
    h = len(M) // 2
    return ([r[:h] for r in M[:h]], [r[h:] for r in M[:h]],
            [r[:h] for r in M[h:]], [r[h:] for r in M[h:]])


def join(C11, C12, C21, C22):
    return [a + b for a, b in zip(C11, C12)] + [a + b for a, b in zip(C21, C22)]


def strassen(X, Y, cutoff=2):
    """Hybrid Strassen: recurse until size <= cutoff, then conventional. n = 2^k."""
    n = len(X)
    if n <= cutoff:
        return conventional(X, Y)
    A11, A12, A21, A22 = split(X)
    B11, B12, B21, B22 = split(Y)
    M1 = strassen(mat_add(A11, A22), mat_add(B11, B22), cutoff)
    M2 = strassen(mat_add(A21, A22), B11, cutoff)
    M3 = strassen(A11, mat_sub(B12, B22), cutoff)
    M4 = strassen(A22, mat_sub(B21, B11), cutoff)
    M5 = strassen(mat_add(A11, A12), B22, cutoff)
    M6 = strassen(mat_sub(A21, A11), mat_add(B11, B12), cutoff)
    M7 = strassen(mat_sub(A12, A22), mat_add(B21, B22), cutoff)
    C11 = mat_add(mat_sub(mat_add(M1, M4), M5), M7)
    C12 = mat_add(M3, M5)
    C21 = mat_add(M2, M4)
    C22 = mat_add(mat_add(mat_sub(M1, M2), M3), M6)
    return join(C11, C12, C21, C22)


def strassen_ops(n, cutoff):
    """(multiplications, additions/subtractions) for hybrid Strassen, n = 2^k."""
    if n <= cutoff:
        return n ** 3, n * n * (n - 1)
    m, a = strassen_ops(n // 2, cutoff)
    return 7 * m, 7 * a + 18 * (n // 2) ** 2


# --------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Module 1: Merge Sort ===")
    orders = [(105, "O1"), (102, "O2"), (105, "O3"), (101, "O4"), (102, "O5"), (103, "O6")]
    tr, cnt = [], [0]
    out = merge_sort(orders, key=lambda o: o[0], trace=tr, counter=cnt)
    for l, r, m in tr:
        print(" merge", l, "+", r, "->", m)
    print(" sorted:", out, "| comparisons =", cnt[0])
    n = 10_000_000
    L = math.ceil(math.log2(n))
    print(f" n lg n = {n*math.log2(n):,.0f}; worst = n*ceil(lg n) - 2^ceil(lg n) + 1 = {n*L - 2**L + 1:,}")

    print("\n=== Module 2: Quick Sort ===")
    s = [42, 17, 63, 8, 55, 29]
    c = [0]
    p = lomuto_partition(s, 0, len(s) - 1, c)
    print(" after one partition:", s, "pivot index", p, "comparisons", c[0])
    n = 100_000
    print(f" worst n(n-1)/2 = {n*(n-1)//2:,}; best ~ n lg n = {n*math.log2(n):,.0f}")
    srt = list(range(1, 2001))
    _, c_first = quick_sort(srt[:], "first")
    _, c_med = quick_sort(srt[:], "median3")
    print(f" sorted n=2000: first-pivot {c_first:,} comps vs median-of-3 {c_med:,} comps")

    print("\n=== Module 3: Binary Search ===")
    ts = [(101, "O4"), (102, "O2"), (102, "O5"), (103, "O6"), (105, "O1"), (105, "O3")]
    for t in (102, 105, 104):
        print(f" key {t}:", binary_search_first(ts, t, key=lambda o: o[0]))
    print(" max comparisons for 10^7 =", math.floor(math.log2(10_000_000)) + 1)

    print("\n=== Module 4: Strassen ===")
    A = [[1, 7], [3, 5]]
    B = [[1, 3], [7, 5]]
    C, M = strassen_2x2(A, B)
    print(" M1..M7 =", M, "\n C =", C, "| conventional =", conventional(A, B))
    n = 1024
    m_full, a_full = strassen_ops(n, 1)
    m_hyb, a_hyb = strassen_ops(n, 64)
    print(f" conventional: mult={n**3:,} add={n*n*(n-1):,} total={n**3+n*n*(n-1):,}")
    print(f" Strassen full: mult={m_full:,} add={a_full:,} total={m_full+a_full:,}")
    print(f" Hybrid cutoff 64: mult={m_hyb:,} add={a_hyb:,} total={m_hyb+a_hyb:,}")
    R = [[random.randint(-9, 9) for _ in range(16)] for _ in range(16)]
    S = [[random.randint(-9, 9) for _ in range(16)] for _ in range(16)]
    assert strassen(R, S, 2) == conventional(R, S)
    print(" 16x16 random Strassen == conventional: OK")
