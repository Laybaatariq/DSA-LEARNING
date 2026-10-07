"""Find the smallest part of a string containing all target characters."""


def minimum_window_substring(source, target):
    """Return the shortest window containing target's characters and counts."""
    if source == "" or target == "":
        return ""

    required_counts = {}

    # Count how many times each target character is needed.
    for character in target:
        if character in required_counts:
            required_counts[character] += 1
        else:
            required_counts[character] = 1

    window_counts = {}
    left = 0
    matched_character_types = 0
    best_start = 0
    best_length = len(source) + 1

    for right in range(len(source)):
        current_character = source[right]

        if current_character in required_counts:
            if current_character in window_counts:
                window_counts[current_character] += 1
            else:
                window_counts[current_character] = 1

            if window_counts[current_character] == required_counts[current_character]:
                matched_character_types += 1

        # When every needed character is present, try to shorten the window.
        while matched_character_types == len(required_counts):
            window_length = right - left + 1

            if window_length < best_length:
                best_start = left
                best_length = window_length

            left_character = source[left]

            if left_character in required_counts:
                window_counts[left_character] -= 1

                if window_counts[left_character] < required_counts[left_character]:
                    matched_character_types -= 1

            left += 1

    if best_length == len(source) + 1:
        return ""

    return source[best_start : best_start + best_length]


examples = [
    ("ADOBECODEBANC", "ABC"),
    ("a", "aa"),
    ("aa", "aa"),
    ("hello world", "ow"),
    ("anything", ""),
]

for source, target in examples:
    result = minimum_window_substring(source, target)

    if result:
        print(f"Smallest window in {source!r} for {target!r}: {result!r}")
    else:
        print(f"No window in {source!r} contains {target!r}")
