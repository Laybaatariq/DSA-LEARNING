"""Reverse the order of words in a sentence."""


def reverse_words(sentence):
    """Return the words in reverse order, separated by single spaces."""
    words = sentence.split()
    reversed_words = []

    index = len(words) - 1

    while index >= 0:
        reversed_words.append(words[index])
        index -= 1

    return " ".join(reversed_words)


examples = [
    "Hello world",
    "Python is fun",
    "  reverse   these words  ",
    "",
]

for sentence in examples:
    result = reverse_words(sentence)
    print(f"{sentence!r} -> {result!r}")