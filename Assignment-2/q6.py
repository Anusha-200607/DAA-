# Question 6: Exhaustive Search for Knapsack

from itertools import product


def exhaustive_knapsack(items, capacity):
    number_of_items = len(items)

    best_value = 0
    best_items = []
    best_weight = 0
    feasible_subsets = 0

    # Generate every possible combination of 0s and 1s.
    # 0 means exclude an item; 1 means include it.
    for selection in product(
        [0, 1], repeat=number_of_items
    ):
        selected_items = []

        total_weight = 0
        total_value = 0

        for i in range(number_of_items):
            if selection[i] == 1:
                name, weight, value = items[i]

                selected_items.append(name)
                total_weight += weight
                total_value += value

        if total_weight <= capacity:
            feasible_subsets += 1

            if total_value > best_value:
                best_value = total_value
                best_weight = total_weight
                best_items = selected_items

    return (
        best_items,
        best_weight,
        best_value,
        feasible_subsets
    )


def main():
    items = [
        ("First Aid Kit", 3, 10),
        ("Water Pack", 4, 12),
        ("Food Pack", 5, 14),
        ("Radio", 2, 7),
        ("Blanket", 3, 8)
    ]

    capacity = 10

    selected, weight, value, feasible = (
        exhaustive_knapsack(items, capacity)
    )

    print("Humanitarian Package Selection")
    print("Capacity:", capacity)

    print("\nAvailable items:")

    for item in items:
        print(item)

    print("\nSelected items:", selected)
    print("Total weight:", weight)
    print("Total value:", value)
    print("Feasible subsets:", feasible)
    print("Total subsets examined:", 2 ** len(items))


if __name__ == "__main__":
    main()
