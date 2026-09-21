"""Check whether two strings are anagrams."""


def are_anagrams(first, second):
    """Return True when both strings contain the same letters."""
    first_normalized = "".join(
        character.lower() for character in first if character.isalnum()
    )
    second_normalized = "".join(
        character.lower() for character in second if character.isalnum()
    )

    return sorted(first_normalized) == sorted(second_normalized)


examples = [
    ("listen", "silent"),
    ("The Eyes", "They See"),
    ("hello", "world"),
]

for first, second in examples:
    result = are_anagrams(first, second)
    print(f"{first!r} and {second!r} -> {result}")