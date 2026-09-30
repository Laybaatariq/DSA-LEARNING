"""Find the first match of a pattern using the KMP algorithm."""


def build_lps_array(pattern):
    """Build the prefix table used to skip unnecessary comparisons."""
    lps = [0] * len(pattern)
    prefix_length = 0
    index = 1

    while index < len(pattern):
        if pattern[index] == pattern[prefix_length]:
            prefix_length += 1
            lps[index] = prefix_length
            index += 1
        elif prefix_length > 0:
            prefix_length = lps[prefix_length - 1]
        else:
            lps[index] = 0
            index += 1

    return lps


def kmp_search(text, pattern):
    """Return the first index of pattern in text, or -1 if it is not found."""
    if pattern == "":
        return 0

    lps = build_lps_array(pattern)
    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                return text_index - pattern_index
        elif pattern_index > 0:
            # Use the prefix table to avoid checking matched characters again.
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1

    return -1


examples = [
    ("ABABCABAB", "ABAB"),
    ("hello world", "world"),
    ("python", "java"),
    ("hello", ""),
]

for text, pattern in examples:
    result = kmp_search(text, pattern)
    print(f"KMP: {pattern!r} in {text!r} -> {result}")