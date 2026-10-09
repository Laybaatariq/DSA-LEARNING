"""Count every palindromic substring in a string."""


def count_from_center(text, left, right):
    """Count palindromes by expanding around one center."""
    palindrome_count = 0

    while left >= 0 and right < len(text):
        if text[left] != text[right]:
            break

        palindrome_count += 1
        left -= 1
        right += 1

    return palindrome_count


def count_palindromic_substrings(text):
    """Return the number of palindromic substring occurrences."""
    total_count = 0

    for center in range(len(text)):
        # Count palindromes with one character in the middle.
        total_count += count_from_center(text, center, center)

        # Count palindromes with two characters in the middle.
        total_count += count_from_center(text, center, center + 1)

    return total_count


examples = [
    "abc",
    "aaa",
    "abba",
    "",
]

for text in examples:
    result = count_palindromic_substrings(text)
    print(f"{text!r} has {result} palindromic substring(s)")
