"""Remove repeated characters that appear next to each other."""


def remove_adjacent_duplicates(text):
    """Keep one character from each consecutive group of repeats."""
    if text == "":
        return ""

    result = text[0]

    # Start at the second character and compare it with the previous one.
    index = 1
    while index < len(text):
        if text[index] != text[index - 1]:
            result += text[index]

        index += 1

    return result


examples = [
    "aaabbccc",
    "bookkeeper",
    "hello",
    "",
]

for text in examples:
    result = remove_adjacent_duplicates(text)
    print(f"{text!r} -> {result!r}")