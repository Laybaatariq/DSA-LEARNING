"""Find all characters that appear only once in a string."""


def find_unique_characters(text):
    """Return characters that appear once, in their original order."""
    character_counts = {}

    # Count how many times each character appears.
    for character in text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    unique_characters = []

    # Add characters whose count is exactly one.
    for character in text:
        if character_counts[character] == 1:
            unique_characters.append(character)

    return unique_characters


examples = [
    "swiss",
    "programming",
    "aabbcc",
]

for text in examples:
    result = find_unique_characters(text)

    if result:
        print(f"{text!r} -> unique characters: {result}")
    else:
        print(f"{text!r} -> no unique characters found")