# Question 3: Brute-Force String Matching

def brute_force_matching(text, pattern):
    comparisons = 0

    if pattern == "":
        return 0, comparisons

    if len(pattern) > len(text):
        return -1, comparisons

    for i in range(len(text) - len(pattern) + 1):
        j = 0

        while j < len(pattern):
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == len(pattern):
            return i, comparisons

    return -1, comparisons


def main():
    test_cases = [
        ("ABABABCABABABC", "ABABC"),
        ("HELLO WORLD", "WORLD"),
        ("COMPUTER SCIENCE", "DATA"),
        ("AAAAAA", "AAA"),
        ("SHORT", "LONGER")
    ]

    for text, pattern in test_cases:
        position, comparisons = brute_force_matching(
            text, pattern
        )

        print("\nText:", text)
        print("Pattern:", pattern)
        print("Position:", position)
        print("Character comparisons:", comparisons)

        if position == -1:
            print("Pattern not found.")
        else:
            print("Pattern found.")


if __name__ == "__main__":
    main()
