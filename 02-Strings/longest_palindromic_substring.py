"""Find the longest palindromic substring."""


def expand_from_center(text, left, right):
    """Return the palindrome found by expanding around a center."""
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1

    return text[left + 1 : right]


def longest_palindromic_substring(text):
    """Return the longest substring that reads the same forward and backward."""
    longest_palindrome = ""

    for center in range(len(text)):
        # A palindrome can have one character in the center.
        odd_palindrome = expand_from_center(text, center, center)

        # A palindrome can also have two characters in the center.
        even_palindrome = expand_from_center(text, center, center + 1)

        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome

        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    return longest_palindrome


examples = [
    "babad",
    "cbbd",
    "racecar",
    "hello",
]

for text in examples:
    result = longest_palindromic_substring(text)
    print(f"{text!r} -> {result!r}")