# Question 7: Closest Pair - Brute Force vs Divide and Conquer

import math
import random


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2
        + (p1[1] - p2[1]) ** 2
    )


def brute_force(points):
    if len(points) < 2:
        return None, float("inf"), 0

    best_distance = float("inf")
    best_pair = None
    comparisons = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            comparisons += 1
            current_distance = distance(
                points[i], points[j]
            )

            if current_distance < best_distance:
                best_distance = current_distance
                best_pair = (points[i], points[j])

    return best_pair, best_distance, comparisons


def merge_by_y(left, right):
    """Merge two lists that are already sorted by y-coordinate."""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def divide_and_conquer(points):
    points = sorted(set(points))

    if len(points) < 2:
        return None, float("inf"), 0

    comparisons = [0]

    def solve(px, py):
        n = len(px)

        # Base case: check every pair in a small group.
        if n <= 3:
            best_distance = float("inf")
            best_pair = None

            for i in range(n):
                for j in range(i + 1, n):
                    comparisons[0] += 1

                    current_distance = distance(
                        px[i], px[j]
                    )

                    if current_distance < best_distance:
                        best_distance = current_distance
                        best_pair = (px[i], px[j])

            return best_pair, best_distance, py

        middle = n // 2

        left_x = px[:middle]
        right_x = px[middle:]

        left_set = set(left_x)

        left_y = [
            point for point in py
            if point in left_set
        ]

        right_y = [
            point for point in py
            if point not in left_set
        ]

        split_x = px[middle][0]

        pair_left, distance_left, sorted_left_y = solve(
            left_x, left_y
        )

        pair_right, distance_right, sorted_right_y = solve(
            right_x, right_y
        )

        if distance_left <= distance_right:
            best_pair = pair_left
            best_distance = distance_left
        else:
            best_pair = pair_right
            best_distance = distance_right

        # Merge the two y-sorted lists in linear time.
        merged_y = merge_by_y(
            sorted_left_y, sorted_right_y
        )

        # Points close enough to the dividing line may
        # contain a better cross-boundary pair.
        strip = [
            point for point in merged_y
            if abs(point[0] - split_x) < best_distance
        ]

        for i in range(len(strip)):
            j = i + 1

            while (
                j < len(strip)
                and strip[j][1] - strip[i][1]
                < best_distance
            ):
                comparisons[0] += 1

                current_distance = distance(
                    strip[i], strip[j]
                )

                if current_distance < best_distance:
                    best_distance = current_distance
                    best_pair = (strip[i], strip[j])

                j += 1

        return best_pair, best_distance, merged_y

    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])

    pair, minimum_distance, _ = solve(
        points_x, points_y
    )

    return pair, minimum_distance, comparisons[0]


def main():
    random.seed(42)

    points = random.sample(
        [
            (x, y)
            for x in range(30)
            for y in range(30)
        ],
        40
    )

    brute_pair, brute_distance, brute_checks = (
        brute_force(points)
    )

    fast_pair, fast_distance, fast_checks = (
        divide_and_conquer(points)
    )

    print("Number of points:", len(points))

    print("\nBrute Force")
    print("Closest pair:", brute_pair)
    print("Minimum distance:", brute_distance)
    print("Distance comparisons:", brute_checks)

    print("\nDivide and Conquer")
    print("Closest pair:", fast_pair)
    print("Minimum distance:", fast_distance)
    print("Distance comparisons:", fast_checks)

    print("\nValidation")
    print(
        "Minimum distances agree:",
        math.isclose(
            brute_distance,
            fast_distance,
            rel_tol=1e-9,
            abs_tol=1e-9
        )
    )

    print("\nComplexity")
    print("Brute Force: O(n^2)")
    print("Divide and Conquer: O(n log n)")


if __name__ == "__main__":
    main()
