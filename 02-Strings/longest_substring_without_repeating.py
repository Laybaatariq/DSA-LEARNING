"""Find the longest substring without repeating characters."""


def longest_substring_without_repeating(text):
    """Return the longest substring containing no repeated characters."""
    longest_substring = ""
    current_substring = ""

    for character in text:
        if character in current_substring:
            repeated_index = current_substring.index(character)
            current_substring = current_substring[repeated_index + 1 :]

        current_substring += character

        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring

    return longest_substring


examples = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "",
]

for text in examples:
    result = longest_substring_without_repeating(text)
    print(f"{text!r} -> {result!r}")