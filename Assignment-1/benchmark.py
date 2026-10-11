import csv
import random
import statistics
import time
from algorithms import (
    linear_search, recursive_binary_search, build_hash_index, hash_search
)

SIZES = [1_000, 10_000, 100_000, 1_000_000]
TRIALS = 5
SEED = 20261011


def median_seconds(fn, trials=TRIALS):
    samples = []
    for _ in range(trials):
        start = time.perf_counter()
        fn()
        samples.append(time.perf_counter() - start)
    return statistics.median(samples)


def main():
    rng = random.Random(SEED)
    rows = []

    for n in SIZES:
        # Unique IDs; the target is deliberately absent to compare worst-case
        # linear search with logarithmic binary search and expected hash lookup.
        records = list(range(100_000_000, 100_000_000 + n))
        rng.shuffle(records)
        missing_target = -1

        sort_time = median_seconds(lambda: sorted(records))
        sorted_records = sorted(records)

        hash_build_time = median_seconds(lambda: build_hash_index(records))
        index = build_hash_index(records)

        # Search timing excludes preprocessing; preprocessing is recorded separately.
        linear_time = median_seconds(lambda: linear_search(records, missing_target))
        binary_time = median_seconds(
            lambda: recursive_binary_search(sorted_records, missing_target)
        )
        hash_time = median_seconds(lambda: hash_search(index, missing_target))

        # Validate correctness for present and absent targets.
        present_target = records[n // 2]
        assert linear_search(records, present_target) != -1
        assert recursive_binary_search(sorted_records, present_target) != -1
        assert hash_search(index, present_target) != -1
        assert linear_search(records, missing_target) == -1
        assert recursive_binary_search(sorted_records, missing_target) == -1
        assert hash_search(index, missing_target) == -1

        rows.extend([
            {"n": n, "algorithm": "Iterative linear search",
             "preprocessing_seconds": 0.0, "search_seconds_median": linear_time,
             "test": "absent target (worst case)"},
            {"n": n, "algorithm": "Recursive binary search",
             "preprocessing_seconds": sort_time, "search_seconds_median": binary_time,
             "test": "absent target (worst case)"},
            {"n": n, "algorithm": "Hash-table lookup",
             "preprocessing_seconds": hash_build_time, "search_seconds_median": hash_time,
             "test": "absent target (expected O(1) lookup)"},
        ])
        print(f"Finished n={n:,}")

    with open("benchmark_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "n", "algorithm", "preprocessing_seconds",
            "search_seconds_median", "test"
        ])
        writer.writeheader()
        writer.writerows(rows)

    print("Saved benchmark_results.csv")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
