"""Find the minimum insertions needed to make a string a palindrome."""


def minimum_insertions_to_make_palindrome(text):
    """Return the minimum number of characters to insert."""
    text_length = len(text)

    if text_length < 2:
        return 0

    # dp[start][end] stores the answer for text[start] through text[end].
    dp = []
    for row_index in range(text_length):
        row = [0] * text_length
        dp.append(row)

    substring_length = 2

    while substring_length <= text_length:
        start = 0

        while start + substring_length <= text_length:
            end = start + substring_length - 1

            if text[start] == text[end]:
                # Matching ends need no new character at those two positions.
                if end - start > 1:
                    dp[start][end] = dp[start + 1][end - 1]
                else:
                    dp[start][end] = 0
            else:
                # Insert a matching character at either end and choose fewer.
                insert_at_start = dp[start + 1][end]
                insert_at_end = dp[start][end - 1]

                if insert_at_start < insert_at_end:
                    dp[start][end] = insert_at_start + 1
                else:
                    dp[start][end] = insert_at_end + 1

            start += 1

        substring_length += 1

    return dp[0][text_length - 1]


examples = [
    "mbadm",
    "race",
    "a",
    "",
]

for text in examples:
    result = minimum_insertions_to_make_palindrome(text)
    print(f"{text!r} -> {result} insertion(s)")