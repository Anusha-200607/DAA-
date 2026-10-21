# Question 5: Brute-Force Convex Hull

def orientation(p, q, r):
    cross_product = (
        (q[0] - p[0]) * (r[1] - p[1])
        - (q[1] - p[1]) * (r[0] - p[0])
    )

    if cross_product > 0:
        return 1       # Counterclockwise

    if cross_product < 0:
        return -1      # Clockwise

    return 0           # Collinear


def convex_hull_bruteforce(points):
    points = sorted(set(points))

    if len(points) <= 2:
        return points, 0

    boundary_vertices = set()
    pair_checks = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p = points[i]
            q = points[j]

            positive = False
            negative = False

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                pair_checks += 1
                side = orientation(p, q, points[k])

                if side > 0:
                    positive = True

                elif side < 0:
                    negative = True

                if positive and negative:
                    break

            # A supporting line has all points on one side.
            if not (positive and negative):
                boundary_vertices.add(p)
                boundary_vertices.add(q)

    # Order the boundary vertices around the hull.
    hull = sorted(boundary_vertices)

    if len(hull) <= 2:
        return hull, pair_checks

    def cross(o, a, b):
        return (
            (a[0] - o[0]) * (b[1] - o[1])
            - (a[1] - o[1]) * (b[0] - o[0])
        )

    lower = []

    for point in hull:
        while (
            len(lower) >= 2
            and cross(lower[-2], lower[-1], point) <= 0
        ):
            lower.pop()

        lower.append(point)

    upper = []

    for point in reversed(hull):
        while (
            len(upper) >= 2
            and cross(upper[-2], upper[-1], point) <= 0
        ):
            upper.pop()

        upper.append(point)

    ordered_hull = lower[:-1] + upper[:-1]

    return ordered_hull, pair_checks


def main():
    test_cases = [
        [
            (0, 0), (4, 0), (4, 4),
            (0, 4), (2, 2)
        ],
        [
            (0, 0), (2, 2), (4, 0),
            (2, 1)
        ],
        [
            (0, 0), (1, 0), (2, 0)
        ],
        [
            (1, 1)
        ],
        []
    ]

    for points in test_cases:
        hull, checks = convex_hull_bruteforce(points)

        print("\nInput points:", points)
        print("Convex hull vertices:", hull)
        print("Point-side checks:", checks)


if __name__ == "__main__":
    main()
