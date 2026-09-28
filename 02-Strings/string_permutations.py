"""Print all permutations of a string."""


def generate_permutations(text):
    """Return all unique permutations of text."""
    if len(text) == 0:
        return [""]

    first_character = text[0]
    remaining_characters = text[1:]
    smaller_permutations = generate_permutations(remaining_characters)
    permutations = []

    for permutation in smaller_permutations:
        for index in range(len(permutation) + 1):
            new_permutation = (
                permutation[:index]
                + first_character
                + permutation[index:]
            )

            if new_permutation not in permutations:
                permutations.append(new_permutation)

    return permutations


examples = [
    "abc",
    "aab",
]

for text in examples:
    print(f"Permutations of {text!r}:")

    for permutation in generate_permutations(text):
        print(permutation)