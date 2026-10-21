# Question 1: Comparison of Sorting Algorithms

import random


def selection_sort(data):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps


def bubble_sort(data):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - 1 - i):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, swaps


def insertion_sort(data):
    arr = data.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, shifts


def main():
    random.seed(10)

    sorted_data = list(range(1, 11))
    reverse_data = sorted_data[::-1]

    nearly_sorted = sorted_data.copy()
    nearly_sorted[4], nearly_sorted[5] = (
        nearly_sorted[5],
        nearly_sorted[4]
    )

    random_data = random.sample(range(1, 100), 10)

    datasets = {
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_data,
        "Nearly Sorted": nearly_sorted,
        "Random": random_data
    }

    algorithms = [
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort)
    ]

    for dataset_name, data in datasets.items():
        print("\nDataset:", dataset_name)
        print("Input:", data)

        for name, algorithm in algorithms:
            result, comparisons, movements = algorithm(data)

            print("\nAlgorithm:", name)
            print("Sorted correctly:", result == sorted(data))
            print("Comparisons:", comparisons)
            print("Swaps or shifts:", movements)


if __name__ == "__main__":
    main()
