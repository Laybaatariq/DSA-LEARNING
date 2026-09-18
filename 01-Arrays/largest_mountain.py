"""Find the longest contiguous mountain in an array."""


def largest_mountain(arr):
    """Return the longest mountain, or an empty list if none exists."""
    longest_mountain = []
    index = 1

    while index < len(arr) - 1:
        # A mountain peak must be greater than both neighboring values.
        if arr[index - 1] < arr[index] > arr[index + 1]:
            left = index - 1
            right = index + 1

            # Extend through the increasing slope.
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            # Extend through the decreasing slope.
            while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                right += 1

            current_mountain = arr[left : right + 1]

            if len(current_mountain) > len(longest_mountain):
                longest_mountain = current_mountain

            # The current mountain has been fully processed.
            index = right
        else:
            index += 1

    return longest_mountain


examples = [
    [2, 1, 4, 7, 3, 2, 5],
    [1, 2, 3, 2, 1],
    [2, 2, 2],
]

for numbers in examples:
    mountain = largest_mountain(numbers)

    if mountain:
        print(f"{numbers} -> largest mountain: {mountain}")
    else:
        print(f"{numbers} -> no mountain found")