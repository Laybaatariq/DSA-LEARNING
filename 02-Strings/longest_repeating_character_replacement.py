"""Find the longest substring after replacing at most k characters."""


def get_highest_character_count(character_counts):
    """Return the largest character count in the current window."""
    highest_count = 0

    for count in character_counts.values():
        if count > highest_count:
            highest_count = count

    return highest_count


def longest_repeating_character_replacement(text, replacements):
    """Return the longest possible substring length after replacements."""
    if replacements < 0:
        raise ValueError("The number of replacements cannot be negative.")

    character_counts = {}
    left = 0
    longest_length = 0

    for right in range(len(text)):
        current_character = text[right]

        if current_character in character_counts:
            character_counts[current_character] += 1
        else:
            character_counts[current_character] = 1

        highest_count = get_highest_character_count(character_counts)
        window_length = right - left + 1

        # If too many characters need replacing, move the left side forward.
        while window_length - highest_count > replacements:
            left_character = text[left]
            character_counts[left_character] -= 1
            left += 1

            highest_count = get_highest_character_count(character_counts)
            window_length = right - left + 1

        if window_length > longest_length:
            longest_length = window_length

    return longest_length


examples = [
    ("AABABBA", 1),
    ("ABAB", 2),
    ("AAAA", 0),
    ("ABC", 0),
]

for text, replacements in examples:
    result = longest_repeating_character_replacement(text, replacements)
    print(f"{text!r} with {replacements} replacement(s) -> {result}")