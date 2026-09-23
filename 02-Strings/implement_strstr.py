"""Implement strstr(), which finds a substring inside another string."""


def strstr(text, pattern):
    """Return the first index of pattern in text, or -1 if not found."""
    if pattern == "":
        return 0

    if len(pattern) > len(text):
        return -1

    start = 0

    while start <= len(text) - len(pattern):
        pattern_index = 0
        match_found = True

        while pattern_index < len(pattern):
            text_character = text[start + pattern_index]
            pattern_character = pattern[pattern_index]

            if text_character != pattern_character:
                match_found = False
                break

            pattern_index += 1

        if match_found:
            return start

        start += 1

    return -1


examples = [
    ("hello world", "world"),
    ("programming", "gram"),
    ("python", "java"),
    ("hello", ""),
]

for text, pattern in examples:
    result = strstr(text, pattern)
    print(f"strstr({text!r}, {pattern!r}) -> {result}")