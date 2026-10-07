"""Count the different non-empty substrings in a string."""


def count_distinct_substrings(text):
    """Return the number of different non-empty substrings."""
    distinct_substrings = set()
    start = 0

    # Try every possible starting position.
    while start < len(text):
        end = start + 1

        # Extend the substring one character at a time.
        while end <= len(text):
            substring = text[start:end]
            distinct_substrings.add(substring)
            end += 1

        start += 1

    return len(distinct_substrings)


examples = [
    "banana",
    "aaa",
    "abc",
    "",
]

for text in examples:
    result = count_distinct_substrings(text)
    print(f"{text!r} has {result} distinct non-empty substring(s)")
