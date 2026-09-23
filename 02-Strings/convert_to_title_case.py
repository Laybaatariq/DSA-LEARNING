"""Convert a sentence to title case."""


def convert_to_title_case(sentence):
    """Return the sentence with the first letter of each word capitalized."""
    words = sentence.split()
    title_case_words = []

    for word in words:
        first_letter = word[0].upper()
        remaining_letters = word[1:].lower()
        title_case_word = first_letter + remaining_letters
        title_case_words.append(title_case_word)

    return " ".join(title_case_words)


examples = [
    "hello world",
    "learning python is fun",
    "THE QUICK BROWN FOX",
]

for sentence in examples:
    result = convert_to_title_case(sentence)
    print(f"{sentence!r} -> {result!r}")