# Design and Analysis of Algorithms — Assignment 1
## Student Record Retrieval: Design, Analysis, and Validation

**Scenario:** Search for a unique student registration number in datasets from 1,000 to 1,000,000+ records. The revised requirement is 50,000 searches per hour and only one daily batch of new records.

> **Experimental honesty:** `benchmark_results.csv` contains timings measured by running `benchmark.py` in this environment. Timings are machine-dependent and should be rerun on the computer used for submission. The benchmark tests an absent target so linear search demonstrates its worst case. Preprocessing is recorded separately from search time.

---

## Task 1 — Design the algorithms (5 marks)

Let `n` be the number of student records and `target` the registration number being searched.

### Approach A: Iterative linear search
**Strategy:** Sequential search. Examine each registration number until a match is found or the list ends. It needs no preprocessing and works on unsorted records.

**Pseudocode**
```text
LINEAR-SEARCH(records, target)
    for i = 0 to length(records) - 1
        if records[i] = target
            return i
    return NOT_FOUND
```

**Selection justification:** This is the simplest baseline and is suitable for very small or unsorted datasets when searches are infrequent. Its disadvantage is that a missing registration number requires examining every record.

### Approach B: Recursive binary search
**Strategy:** Divide and conquer. First sort the records by registration number. Compare the target with the middle value and recursively continue in only the half that can contain the target.

**Preprocessing:** Sorting costs `Θ(n log n)` with a comparison-based efficient sort. If the original data must remain unchanged, create a sorted copy.

**Pseudocode**
```text
RECURSIVE-BINARY-SEARCH(A, target, left, right)
    if left > right
        return NOT_FOUND
    mid = floor((left + right) / 2)
    if A[mid] = target
        return mid
    else if target < A[mid]
        return RECURSIVE-BINARY-SEARCH(A, target, left, mid - 1)
    else
        return RECURSIVE-BINARY-SEARCH(A, target, mid + 1, right)
```

**Selection justification:** This provides a recursive divide-and-conquer strategy and reduces the search range by half at each call. It is efficient when the data can be kept sorted. Insertions into a sorted array can be costly, but daily batch updates make rebuilding the sorted index practical.

### Approach C: Hash-table lookup
**Strategy:** Build an index mapping each registration number to its record position (or directly to its record). Then use the registration number as a key.

**Preprocessing:** Build the hash index once after the daily update batch. Building it takes expected `Θ(n)` time and `Θ(n)` additional space.

**Pseudocode**
```text
BUILD-HASH-INDEX(records)
    index = empty hash table
    for each record in records
        index[record.registration_number] = record
    return index

HASH-SEARCH(index, target)
    if target is a key in index
        return index[target]
    return NOT_FOUND
```

**Selection justification:** Hash lookup has expected `Θ(1)` search time and is attractive for many searches between updates. Its limitations include extra memory, hash collisions, and `Θ(n)` worst-case lookup under severe collision conditions. Registration numbers must be unique or duplicate handling must be defined.

---

## Task 2 — Identify the basic operation (2 marks)

- **Linear search:** Compare `records[i]` with `target`. This comparison determines whether the algorithm stops or advances. For a missing target, it executes exactly `n` times; for a target at zero-based position `k`, it executes `k + 1` times.
- **Recursive binary search:** Compare the middle registration number with the target, then determine which half remains. Each unsuccessful call reduces the candidate interval to at most half its former size, so the number of comparisons grows logarithmically.
- **Hash-table lookup:** The basic operation is the hash-table key lookup (hashing the key and checking the corresponding bucket/slot). It takes expected constant time under a suitable hash function and controlled load factor, but collisions can increase the work.

These operations are appropriate because they dominate the repeated work during a search and their counts can be related directly to `n`.

---

## Task 3 — Derive time-complexity functions mathematically (6 marks)

### A. Iterative linear search
Let `C(n)` be the number of equality comparisons.

- Best case: target is the first item, so `C(n) = 1`.
- Worst case: target is absent or last, so `C(n) = n`.
- If the target is equally likely to be at any of the `n` positions, average comparisons are:
  `Cavg(n) = (1 + 2 + ... + n) / n = [n(n + 1)/2] / n = (n + 1)/2`.

Therefore, best-case time is `Θ(1)` and average/worst-case search time is `Θ(n)`. There is no preprocessing cost. Total cost for `q` searches is `Θ(qn)` in the worst case.

### B. Recursive binary search
After sorting, let `C(n)` be the worst-case number of comparisons. Each call performs constant work and recurses on at most half the array:

`C(n) = C(floor(n/2)) + c`, for `n > 1`, with `C(1) = c0`.

After `k` halvings, the remaining interval is approximately `n / 2^k`. Stop when it is at most 1:

`n / 2^k ≤ 1`  
`2^k ≥ n`  
`k ≥ log₂ n`.

Thus the search uses `Θ(log n)` comparisons. Sorting adds `Θ(n log n)`, so one-time build-and-search cost is `Θ(n log n) + Θ(log n) = Θ(n log n)`. For `q` searches after a single sort, the total is `Θ(n log n + q log n)`. If sorted data is already maintained, each search costs `Θ(log n)`.

### C. Hash-table lookup
Building the index visits each record once, so expected build time is:

`B(n) = b n = Θ(n)`.

With a suitable hash function and controlled load factor, expected lookup work is approximately constant, `H(n) = h = Θ(1)`. Therefore, build plus one lookup is expected `Θ(n) + Θ(1) = Θ(n)`. For `q` lookups between updates, total expected cost is `Θ(n + q)`. The theoretical worst-case lookup can be `Θ(n)` if many keys collide; worst-case build-and-lookup is then `O(n)` for one lookup and potentially `O(n²)` for inserting all keys into a badly colliding chained table. The expected result assumes normal hash-table behavior.

---

## Task 4 — Best, average, and worst cases (4 marks)

| Algorithm | Best case | Average case | Worst case | Conditions |
|---|---|---|---|---|
| Iterative linear search | `Θ(1)` | `Θ(n)` | `Θ(n)` | Best if first item matches; worst if absent or last |
| Recursive binary search (sorted) | `Θ(1)` | `Θ(log n)` | `Θ(log n)` | Best if middle item matches; otherwise interval is halved repeatedly |
| Hash-table lookup | Expected `Θ(1)` | Expected `Θ(1)` | `Θ(n)` | Best/typical with few collisions; worst when collisions force many key checks |

For linear search, a missing target always causes `n` comparisons. For binary search, the search interval halves regardless of the target's position, unless the middle item matches immediately. For hashing, average and expected performance depend on hash distribution and load factor, so constant time is not an unconditional worst-case guarantee.

---

## Task 5 — Asymptotic analysis (3 marks)

| Algorithm | Search growth | Preprocessing | Overall build + one search |
|---|---:|---:|---:|
| Linear search | `Θ(n)` worst/average | `Θ(1)` | `Θ(n)` |
| Recursive binary search | `Θ(log n)` | Sorting `Θ(n log n)` | `Θ(n log n)` |
| Hash table | Expected `Θ(1)` | Expected build `Θ(n)` | Expected `Θ(n)` |

`O` is an asymptotic upper bound, `Ω` a lower bound, and `Θ` a tight bound when both upper and lower bounds match. A linear search's worst-case time is `Θ(n)`. Binary search is `Θ(log n)` per search once sorted. Hash lookup is expected `Θ(1)` but worst-case `Θ(n)`.

For scale, increasing from 1,000 to 1,000,000 records multiplies `n` by 1,000. A worst-case linear search can require 1,000 times as many comparisons. Binary search increases from about 10 to about 20 halvings. Expected hash lookup remains approximately constant, although its index requires memory and construction.

---

## Task 6 — Formulate the recurrence (3 marks)

For recursive binary search, the original input contains `n` sorted records. One recursive call searches at most half the remaining records; there is one recursive call per non-base case. The work outside the recursive call consists of a middle-index calculation, a constant number of comparisons, and a branch, represented by constant `c`.

Base case: the interval is empty (`left > right`) or a one-element interval is checked.

For a simplified worst-case recurrence:

`T(n) = T(floor(n/2)) + c`, for `n > 1`  
`T(1) = c0`  
`T(0) = c0`

The recurrence follows directly from one half-size recursive subproblem plus constant non-recursive work.

---

## Task 7 — Solve the recurrence (4 marks)

Use the iteration method. For clarity, assume `n` is a power of two and write `T(n) = T(n/2) + c`.

`T(n) = T(n/2) + c`  
`= T(n/4) + 2c`  
`= T(n/8) + 3c`  
After `k` expansions: `T(n) = T(n/2^k) + kc`.

The recursion reaches size 1 when `n/2^k = 1`, so `k = log₂ n`.

Substitute:

`T(n) = T(1) + c log₂ n = c0 + c log₂ n`.

Hence `T(n) = Θ(log n)`. The iteration method applies because each call reduces the input by a factor of two and does constant additional work. This means that doubling the sorted dataset adds only about one extra binary-search comparison level. Sorting cost is separate and is `Θ(n log n)`.

---

## Task 8 — Implement and test (4 marks)

The repository contains `algorithms.py` and `benchmark.py`.

Run with Python 3:
```bash
python benchmark.py
```

The benchmark creates unique registration numbers at sizes 1,000, 10,000, 100,000, and 1,000,000; shuffles each dataset; and tests an absent key (`-1`) to measure the worst case for linear search. It uses the same records for all approaches. It measures sorting time, hash-index build time, and median search time separately. Five timing trials are used, with a fixed random seed for repeatability.

Correctness tests check both a present registration number and an absent registration number for all algorithms. For an additional manual test, change the target to the first, middle, last, and missing registration numbers.

---

## Task 9 — Experimental performance (3 marks)

Measured values are in `benchmark_results.csv`. `preprocessing_seconds` records sorting or hash-index construction, while `search_seconds_median` records median search time over five trials. The test is an absent target, so the linear-search measurement is its worst-case scan. Binary search and hash lookup also return not-found.

Run `python benchmark.py` on your own computer before final submission and commit the newly generated CSV. If you need a graph, plot the CSV values after running the benchmark; use a logarithmic vertical axis because timings differ substantially. Do not claim that one machine's exact seconds are universal.

---

## Task 10 — Compare theory with experiment (4 marks)

The expected pattern is that linear-search time increases roughly in proportion to `n`, recursive binary-search time increases slowly as `log₂ n`, and hash lookup stays approximately flat on average. Sorting and hash-index construction increase with dataset size and must not be omitted from the total-cost comparison.

Measured timings may deviate from ideal curves because of interpreter overhead, CPU scheduling, memory/cache behavior, allocation and garbage collection, hash collisions, and timer resolution. At small `n`, fixed overhead can dominate. The benchmark uses an absent key to make linear search's worst-case operation count predictable. Use the CSV generated on the submission computer to state whether the measured trend agrees with theory; do not infer exact timings from Big-O alone.

---

## Task 11 — Recommend and defend the design (4 marks)

For an evolving student-record system with many searches, use a hash-table index keyed by unique registration number as the primary lookup structure, provided memory is available and the implementation handles collisions and uniqueness correctly. Its expected lookup time is `Θ(1)` and index construction is expected `Θ(n)`. Since updates occur in a daily batch, rebuild or update the index once after that batch rather than paying the build cost for every search.

Keep a sorted view or database index if ordered reports and range queries are also needed. Binary search is a strong alternative when sorted data is already maintained and deterministic `Θ(log n)` search is preferred. Linear search is not recommended for one million records and high request volume because its worst-case work is `Θ(n)` per request.

The recommendation should be supported by the CSV timings collected on the target machine. Limitations of hashing are extra memory, collision-dependent worst-case behavior, and the need to rebuild/update the index consistently after daily changes.

---

## Task 12 — Day-4 design challenge (8 marks)

### A. Impact analysis (2 marks)
The database now has 1,000,000 records and receives 50,000 searches per hour, while new records are added only once per day. This is about `50,000 / 3,600 ≈ 13.9` searches per second on average, or `50,000 × 24 = 1,200,000` searches per day if the hourly rate continues all day. The dominant cost is repeated lookup, not daily record insertion. The low update frequency makes it practical to build an index once per daily batch and reuse it for many queries.

### B. Evaluate the original design (2 marks)
A sorted-array binary search needs about `log₂(1,000,000) ≈ 19.93`, or roughly 20 comparison levels per search. Across 50,000 searches, that is roughly one million comparison levels per hour, after sorting. Hash lookup is expected constant time per search, so 50,000 searches involve approximately 50,000 key lookups plus one daily index build. Linear search could scan up to 1,000,000 records per missing-key query, producing up to `50,000 × 1,000,000 = 50,000,000,000` comparisons per hour. Therefore, linear search is unsuitable.

### C. Adaptation/redesign (2 marks)
**Decision: modify the design to use a hash index as the primary registration-number lookup.** At the end of each daily update batch, build or refresh the mapping from registration number to record. Serve searches from this in-memory index, with persistence and recovery handled by the underlying database. If the application also needs sorted listing or range queries, maintain a sorted index as a secondary structure.

Expected total work per day is `Θ(n + Q)` for hash-index build plus `Q` expected constant-time lookups, where `Q` is the day's number of searches. Binary search would cost `Θ(n log n + Q log n)` if sorting must be repeated each day, or `Θ(Q log n)` when the sorted index is already maintained.

### D. Evidence-based defence (2 marks)
At one million records and 50,000 queries per hour, a one-time `Θ(n)` daily index build is amortized across a large number of expected `Θ(1)` lookups. Binary search is also practical at about 20 comparisons per query, but hash lookup is expected to perform fewer key probes for exact-match searches. The included benchmark separates preprocessing from search time so this trade-off can be judged using measured evidence. The final production choice must also consider memory use, collision handling, availability, and database consistency. Rerun the benchmark on the target machine and use those actual results as the experimental evidence.

---

## Conclusion

For small or infrequent searches, iterative linear search is simple but scales poorly. Recursive binary search is efficient when records are sorted. For the stated workload—one million records, 50,000 exact-match searches per hour, and daily updates—a hash-table index is the recommended primary lookup strategy because expected lookup is constant-time and the index build can be amortized over many searches.

## Repository files

- `README.md` — answers to Tasks 1–12.
- `algorithms.py` — the three implementations.
- `benchmark.py` — reproducible benchmark and correctness checks.
- `benchmark_results.csv` — measured performance output.
- `performance_plot.png` — chart generated from the measured results.
