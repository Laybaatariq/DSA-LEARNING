"""Check whether one string is a rotation of another."""


def is_rotation(first, second):
    """Return True when second is a rotation of first."""
    if len(first) != len(second):
        return False

    combined_string = first + first

    return second in combined_string


examples = [
    ("waterbottle", "erbottlewat"),
    ("abcd", "cdab"),
    ("abcd", "acbd"),
    ("hello", "hello"),
]

for first, second in examples:
    result = is_rotation(first, second)
    print(f"{second!r} is a rotation of {first!r}: {result}")