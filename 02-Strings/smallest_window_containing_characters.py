"""Find the smallest substring containing all characters of another string."""


def smallest_window_containing_all_characters(text, target):
    """Return the shortest window containing target's characters and counts."""
    if text == "" or target == "":
        return ""

    required_counts = {}

    # Count how many times each character is needed.
    for character in target:
        if character in required_counts:
            required_counts[character] += 1
        else:
            required_counts[character] = 1

    window_counts = {}
    left = 0
    matched_character_types = 0
    best_start = 0
    best_length = len(text) + 1

    for right in range(len(text)):
        current_character = text[right]

        if current_character in required_counts:
            if current_character in window_counts:
                window_counts[current_character] += 1
            else:
                window_counts[current_character] = 1

            if window_counts[current_character] == required_counts[current_character]:
                matched_character_types += 1

        # Once all required characters are present, shorten the window.
        while matched_character_types == len(required_counts):
            current_length = right - left + 1

            if current_length < best_length:
                best_start = left
                best_length = current_length

            left_character = text[left]

            if left_character in required_counts:
                window_counts[left_character] -= 1

                if window_counts[left_character] < required_counts[left_character]:
                    matched_character_types -= 1

            left += 1

    if best_length == len(text) + 1:
        return ""

    return text[best_start : best_start + best_length]


examples = [
    ("ADOBECODEBANC", "ABC"),
    ("a", "aa"),
    ("aa", "aa"),
    ("hello world", "ow"),
    ("anything", ""),
]

for text, target in examples:
    result = smallest_window_containing_all_characters(text, target)

    if result:
        print(f"Smallest window in {text!r} for {target!r}: {result!r}")
    else:
        print(f"No window in {text!r} contains {target!r}")
