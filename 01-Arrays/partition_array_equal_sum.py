"""Partition an array into two contiguous subarrays with equal sums."""


def partition_equal_sum(arr):
    """Return two non-empty equal-sum subarrays, or None if impossible."""
    if len(arr) < 2:
        return None

    total_sum = sum(arr)
    left_sum = 0

    # The last element must remain in the right subarray.
    for index in range(len(arr) - 1):
        left_sum += arr[index]
        right_sum = total_sum - left_sum

        if left_sum == right_sum:
            return arr[: index + 1], arr[index + 1 :]

    return None


examples = [
    [1, 2, 3, 3],
    [2, 4, 2, 4],
    [1, 2, 3],
]

for numbers in examples:
    result = partition_equal_sum(numbers)

    if result is None:
        print(f"{numbers} cannot be partitioned into equal-sum subarrays")
    else:
        left, right = result
        print(f"{numbers} -> {left} and {right}")