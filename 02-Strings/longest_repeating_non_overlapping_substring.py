"""Find the longest substring that appears twice without overlapping."""


def longest_repeating_non_overlapping_substring(text):
    """Return the longest substring that occurs twice in separate positions."""
    text_length = len(text)

    # matching_lengths[first_end][second_end] stores the length of the
    # matching substrings that end just before these two positions.
    matching_lengths = []
    for _ in range(text_length + 1):
        matching_lengths.append([0] * (text_length + 1))

    longest_substring = ""

    # Compare each pair of positions. The second position must come later.
    for first_end in range(1, text_length + 1):
        for second_end in range(first_end + 1, text_length + 1):
            first_character = text[first_end - 1]
            second_character = text[second_end - 1]

            if first_character == second_character:
                matching_length = matching_lengths[first_end - 1][second_end - 1] + 1

                # Keep the two matching copies from sharing any characters.
                distance_between_ends = second_end - first_end
                if matching_length > distance_between_ends:
                    matching_length = distance_between_ends

                matching_lengths[first_end][second_end] = matching_length

                if matching_length > len(longest_substring):
                    start_of_substring = first_end - matching_length
                    longest_substring = text[
                        start_of_substring:first_end
                    ]

    return longest_substring


examples = [
    "banana",
    "aaaa",
    "abcab",
    "abcdef",
    "",
]

for text in examples:
    result = longest_repeating_non_overlapping_substring(text)

    if result:
        print(f"Longest non-overlapping repeat in {text!r}: {result!r}")
    else:
        print(f"No non-overlapping repeated substring in {text!r}")
