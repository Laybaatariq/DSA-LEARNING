"""Find the first character that appears only once in a string."""


def count_characters(text):
    """Count how many times each character appears."""
    character_counts = {}

    for character in text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts


def first_non_repeating_character(text):
    """Return the first character that appears exactly once, or None."""
    character_counts = count_characters(text)

    # Check characters in their original order.
    for character in text:
        if character_counts[character] == 1:
            return character

    return None


examples = [
    "swiss",
    "programming",
    "aabbcc",
]

for text in examples:
    result = first_non_repeating_character(text)

    if result is None:
        print(f"{text!r} -> no non-repeating character found")
    else:
        print(f"{text!r} -> first non-repeating character: {result!r}")