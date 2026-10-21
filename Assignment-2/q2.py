# Question 2: Sequential Search

def sequential_search(data, target):
    comparisons = 0

    for index in range(len(data)):
        comparisons += 1

        if data[index] == target:
            return index, comparisons

    return -1, comparisons


def main():
    test_cases = [
        ([10, 20, 30, 40, 50], 10, "First element"),
        ([10, 20, 30, 40, 50], 30, "Middle element"),
        ([10, 20, 30, 40, 50], 50, "Last element"),
        ([10, 20, 30, 40, 50], 99, "Unsuccessful search"),
        ([], 10, "Empty list")
    ]

    for data, target, description in test_cases:
        index, comparisons = sequential_search(data, target)

        print("\nTest:", description)
        print("List:", data)
        print("Target:", target)
        print("Result index:", index)
        print("Comparisons:", comparisons)

    print("\nComparison with increasing input sizes:")

    for size in [10, 100, 1000, 5000]:
        data = list(range(size))

        index, comparisons = sequential_search(
            data, size - 1
        )

        print(
            "Size:", size,
            "| Index:", index,
            "| Comparisons:", comparisons
        )


if __name__ == "__main__":
    main()
