"""Make the shortest palindrome by adding characters to the front."""


def shortest_palindrome(text):
    """Return the shortest palindrome made by adding characters to the front."""
    combined = []

    # A palindromic prefix matches the reverse of the string from its start.
    for character in text:
        combined.append(character)

    # None is used as a separator, so it cannot match a string character.
    combined.append(None)

    index = len(text) - 1
    while index >= 0:
        combined.append(text[index])
        index -= 1

    # Build the KMP prefix table for the combined character list.
    prefix_table = [0] * len(combined)
    prefix_length = 0
    index = 1

    while index < len(combined):
        if combined[index] == combined[prefix_length]:
            prefix_length += 1
            prefix_table[index] = prefix_length
            index += 1
        elif prefix_length > 0:
            prefix_length = prefix_table[prefix_length - 1]
        else:
            prefix_table[index] = 0
            index += 1

    # The final prefix-table value is the longest palindromic prefix length.
    palindrome_prefix_length = prefix_table[-1]
    remaining_suffix = text[palindrome_prefix_length:]
    characters_to_add = remaining_suffix[::-1]

    return characters_to_add + text


examples = [
    "aacecaaa",
    "abcd",
    "racecar",
    "",
    "#aba",
]

for text in examples:
    result = shortest_palindrome(text)
    print(f"{text!r} -> {result!r}")
