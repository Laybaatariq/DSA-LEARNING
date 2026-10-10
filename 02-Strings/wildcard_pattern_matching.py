"""Match text against a pattern containing ? and * wildcards."""


def wildcard_pattern_matches(text, pattern):
    """Return True if the whole text matches the whole wildcard pattern.

    In the pattern:
    - ? matches exactly one character.
    - * matches any number of characters, including none.
    """
    text_length = len(text)
    pattern_length = len(pattern)

    # matches[i][j] tells us whether the first i text characters match
    # the first j pattern characters.
    matches = []
    for _ in range(text_length + 1):
        matches.append([False] * (pattern_length + 1))

    # Two empty strings match.
    matches[0][0] = True

    # A pattern made of stars can match an empty text.
    for pattern_end in range(1, pattern_length + 1):
        if pattern[pattern_end - 1] == "*":
            matches[0][pattern_end] = matches[0][pattern_end - 1]

    for text_end in range(1, text_length + 1):
        for pattern_end in range(1, pattern_length + 1):
            pattern_character = pattern[pattern_end - 1]
            text_character = text[text_end - 1]

            if pattern_character == "*":
                # The star either matches nothing, or takes one more character.
                matches[text_end][pattern_end] = (
                    matches[text_end][pattern_end - 1]
                    or matches[text_end - 1][pattern_end]
                )
            elif pattern_character == "?" or pattern_character == text_character:
                # A normal match or ? uses one character from each string.
                matches[text_end][pattern_end] = matches[text_end - 1][pattern_end - 1]

    return matches[text_length][pattern_length]


examples = [
    ("adceb", "*a*b"),
    ("acdcb", "a*c?b"),
    ("hello", "h?llo"),
    ("hello", "h*o"),
    ("", "*"),
    ("abc", "a*d"),
]

for text, pattern in examples:
    result = wildcard_pattern_matches(text, pattern)
    print(f"{text!r} matches {pattern!r}: {result}")
