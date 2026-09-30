"""Find the first match of a pattern using the Rabin-Karp algorithm."""


def rabin_karp_search(text, pattern):
    """Return the first index of pattern in text, or -1 if it is not found."""
    if pattern == "":
        return 0

    text_length = len(text)
    pattern_length = len(pattern)

    if pattern_length > text_length:
        return -1

    base = 256
    modulus = 101
    highest_place_value = 1
    pattern_hash = 0
    window_hash = 0

    # Calculate the value of the highest character place in each hash.
    position = 0
    while position < pattern_length - 1:
        highest_place_value = (highest_place_value * base) % modulus
        position += 1

    # Calculate the starting hashes for the pattern and the first text window.
    position = 0
    while position < pattern_length:
        pattern_hash = (
            (base * pattern_hash + ord(pattern[position])) % modulus
        )
        window_hash = (
            (base * window_hash + ord(text[position])) % modulus
        )
        position += 1

    start = 0

    while start <= text_length - pattern_length:
        if pattern_hash == window_hash:
            # Hashes can collide, so compare the actual characters too.
            characters_match = True
            offset = 0

            while offset < pattern_length:
                if text[start + offset] != pattern[offset]:
                    characters_match = False
                    break
                offset += 1

            if characters_match:
                return start

        # Move the text window one character to the right.
        if start < text_length - pattern_length:
            old_character = ord(text[start])
            new_character = ord(text[start + pattern_length])

            window_hash = (
                base * (window_hash - old_character * highest_place_value)
                + new_character
            ) % modulus

            # Keep the hash non-negative after removing the old character.
            if window_hash < 0:
                window_hash += modulus

        start += 1

    return -1


examples = [
    ("ABABCABAB", "ABAB"),
    ("hello world", "world"),
    ("python", "java"),
    ("hello", ""),
]

for text, pattern in examples:
    result = rabin_karp_search(text, pattern)
    print(f"Rabin-Karp: {pattern!r} in {text!r} -> {result}")