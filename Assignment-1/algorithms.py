"""
Student Registration Number Search Algorithms
Python 3.10+
Three distinct strategies:
1. Iterative linear search
2. Recursive binary search (requires sorted data)
3. Hash-table lookup (requires index construction)
"""

def linear_search(records, target):
    """Return index of target in records, or -1. O(n) worst case."""
    for i, value in enumerate(records):
        if value == target:
            return i
    return -1


def recursive_binary_search(sorted_records, target, left=0, right=None):
    """Return index of target in sorted_records, or -1. O(log n) search."""
    if right is None:
        right = len(sorted_records) - 1
    if left > right:
        return -1

    mid = (left + right) // 2
    if sorted_records[mid] == target:
        return mid
    if target < sorted_records[mid]:
        return recursive_binary_search(sorted_records, target, left, mid - 1)
    return recursive_binary_search(sorted_records, target, mid + 1, right)


def build_hash_index(records):
    """Build registration-number -> record-position index. Expected O(n)."""
    return {registration: i for i, registration in enumerate(records)}


def hash_search(index, target):
    """Return stored position or -1. Expected O(1), worst-case O(n)."""
    return index.get(target, -1)
