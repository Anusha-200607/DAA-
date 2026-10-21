# Question 4: Brute-Force Closest Pair of Points

import math
from itertools import combinations


def closest_pair(points):
    if len(points) < 2:
        return None, None, 0

    minimum_distance = float("inf")
    best_pair = None
    comparisons = 0

    for point1, point2 in combinations(points, 2):
        comparisons += 1

        distance = math.sqrt(
            (point1[0] - point2[0]) ** 2
            + (point1[1] - point2[1]) ** 2
        )

        if distance < minimum_distance:
            minimum_distance = distance
            best_pair = (point1, point2)

    return best_pair, minimum_distance, comparisons


def main():
    test_cases = [
        [(0, 0), (3, 4), (1, 1), (8, 8)],
        [(0, 0), (0, 2), (2, 0), (2, 2)],
        [(1, 1), (1, 1), (5, 5)],
        [(2, 3)],
        []
    ]

    for points in test_cases:
        pair, distance, comparisons = closest_pair(points)

        print("\nPoints:", points)
        print("Closest pair:", pair)
        print("Minimum distance:", distance)
        print("Pair comparisons:", comparisons)

        n = len(points)
        expected_pairs = n * (n - 1) // 2

        print("Expected number of pairs:", expected_pairs)


if __name__ == "__main__":
    main()
