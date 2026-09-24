"""Count how many times a character appears in a string."""


def count_character(text, target_character):
    """Return the number of times target_character appears in text."""
    count = 0

    for character in text:
        if character == target_character:
            count += 1

    return count


examples = [
    ("hello world", "l"),
    ("programming", "m"),
    ("banana", "a"),
]

for text, target_character in examples:
    result = count_character(text, target_character)
    print(f"{target_character!r} appears {result} time(s) in {text!r}")