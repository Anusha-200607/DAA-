# CSA06 – CO3 Case Study: Divide-and-Conquer Engine of "KartIQ"

**Course:** CSA06 – Design and Analysis of Algorithms
**Assessment:** CO3 – Case Study (Individual)
**Student:** Anusha  |  **Reg. No.:** 192465016

This repository contains my solution to the CO3 case study on redesigning four slow modules of a retail analytics platform (KartIQ) with divide-and-conquer algorithms.

## Repository contents

| File | Description |
|------|-------------|
| `CSA06_CO3_Case_Study_Anusha.docx` | The completed assessment report, parts (a) to (f), with traces, recurrences and calculations |
| `kartiq_algorithms.py` | Python implementations used to check every trace and number in the report |
| `README.md` | This file |

## Summary of the design

| Module | Problem | Algorithm chosen | Time | Extra memory |
|--------|---------|------------------|------|--------------|
| 1 – Nightly order consolidation | Sort 10,000,000 orders by timestamp, keep arrival order of ties | Stable **Merge Sort** (external k-way merge if data exceeds RAM) | Θ(n log n), at most 223,222,785 comparisons | Θ(n) |
| 2 – Live seller leaderboard | Re-sort 100,000 nearly sorted scores every few seconds | **Quick Sort** with **median-of-three** pivot (+ insertion sort for small parts, introsort fallback) | Θ(n log n) average, about 2 × 10⁶ comparisons (first-element pivot: about 5 × 10⁹) | O(log n) |
| 3 – Order lookup | Find the first order with a given timestamp | **Binary Search** (first-occurrence variant) | Θ(log n), at most 24 comparisons | O(1) |
| 4 – Recommendation scores | C = A × B with n = 1,024 | **Hybrid Strassen** (cutoff 64, conventional kernel below) | Θ(n^2.807); 629,407,744 multiplications vs 1,073,741,824 | Θ(n²) |

### Key results

- **Module 1:** the sample orders sort in 10 comparisons; equal timestamps keep arrival order (O2 before O5, O1 before O3).
- **Module 2:** one partition of `42, 17, 63, 8, 55, 29` gives `29, 17, 8 | 42 | 55, 63`. On sorted input of 2,000 elements the first-element pivot used 1,999,000 comparisons against 17,964 for median-of-three.
- **Module 3:** the first-occurrence search returns O2 for timestamp 102 and O1 for 105, in 3 iterations each.
- **Module 4:** Strassen on the 2 × 2 sample gives `[[50, 38], [38, 34]]`, the same as the conventional product. Full-depth Strassen saves only about 8.2% of all operations at n = 1,024; the hybrid saves about 39.4%.

## How to run the code

Requires Python 3.8 or later and no external packages.

```bash
python kartiq_algorithms.py
```

The script prints the merge trace and comparison count, the quick sort partition, the binary search traces, the Strassen products and operation counts, and checks Strassen against the conventional method on a random 16 × 16 matrix.

## Notes

- Comparison and operation counts are exact for the stated models (key comparisons; scalar multiplications and additions). Times quoted in the report assume 10⁹ simple operations per second and are only illustrative.
- The Python file is a verification aid for the report; the report itself is the assessment submission.
