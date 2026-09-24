"""Remove all spaces from a string."""


def remove_spaces(text):
    """Return the string without spaces or other whitespace characters."""
    text_without_spaces = ""

    for character in text:
        if not character.isspace():
            text_without_spaces += character

    return text_without_spaces


examples = [
    "hello world",
    "Learning Python is fun",
    "remove  extra   spaces",
]

for text in examples:
    result = remove_spaces(text)
    print(f"{text!r} -> {result!r}")