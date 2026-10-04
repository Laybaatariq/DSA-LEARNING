"""Find the longest dictionary word formed by deleting characters."""


def is_subsequence(word, text):
    """Check whether word's characters appear in order inside text."""
    word_index = 0
    text_index = 0

    while word_index < len(word) and text_index < len(text):
        if word[word_index] == text[text_index]:
            word_index += 1

        text_index += 1

    return word_index == len(word)


def find_longest_word(text, dictionary):
    """Return the longest dictionary word that can be formed from text."""
    longest_word = ""

    for word in dictionary:
        if is_subsequence(word, text):
            if len(word) > len(longest_word):
                longest_word = word
            elif len(word) == len(longest_word) and word < longest_word:
                # If lengths tie, choose the alphabetically first word.
                longest_word = word

    return longest_word


examples = [
    ("abpcplea", ["ale", "apple", "monkey", "plea"]),
    ("bab", ["ba", "ab", "b"]),
    ("abc", ["xyz", "longer"]),
]

for text, dictionary in examples:
    result = find_longest_word(text, dictionary)

    if result:
        print(f"From {text!r}, the longest dictionary word is {result!r}")
    else:
        print(f"No dictionary word can be formed from {text!r}")