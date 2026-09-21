"""Check whether two strings are anagrams."""


def clean_string(text):
    """Remove spaces and punctuation, then convert letters to lowercase."""
    cleaned_text = ""

    for character in text:
        if character.isalnum():
            cleaned_text += character.lower()

    return cleaned_text


def count_characters(text):
    """Count how many times each character appears in a string."""
    character_counts = {}

    for character in text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts


def are_anagrams(first, second):
    """Return True when both strings contain the same characters."""
    first_cleaned = clean_string(first)
    second_cleaned = clean_string(second)

    first_counts = count_characters(first_cleaned)
    second_counts = count_characters(second_cleaned)

    return first_counts == second_counts


examples = [
    ("listen", "silent"),
    ("The Eyes", "They See"),
    ("hello", "world"),
]

for first, second in examples:
    result = are_anagrams(first, second)
    print(f"{first!r} and {second!r} -> {result}")