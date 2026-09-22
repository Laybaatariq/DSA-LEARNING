"""Check whether a string is a palindrome."""


def is_palindrome(text):
    """Return True when the string reads the same forward and backward."""
    cleaned_text = ""

    # Keep only letters and numbers, and use lowercase characters.
    for character in text:
        if character.isalnum():
            cleaned_text += character.lower()

    reversed_text = ""
    index = len(cleaned_text) - 1

    # Build the reversed string one character at a time.
    while index >= 0:
        reversed_text += cleaned_text[index]
        index -= 1

    return cleaned_text == reversed_text


examples = [
    "madam",
    "racecar",
    "hello",
    "A man, a plan, a canal: Panama",
]

for text in examples:
    result = is_palindrome(text)
    print(f"{text!r} -> {result}")