"""Reverse a string."""


def reverse_string(text):
    """Return the string in reverse order."""
    return text[::-1]


examples = [
    "hello",
    "Python",
    "Replit",
]

for text in examples:
    print(f"{text} -> {reverse_string(text)}")