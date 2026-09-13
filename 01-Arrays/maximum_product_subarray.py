def max_product_subarray(numbers):
    """Return the largest product of any contiguous subarray."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    current_max = numbers[0]
    current_min = numbers[0]
    maximum_product = numbers[0]

    for number in numbers[1:]:
        if number < 0:
            current_max, current_min = current_min, current_max

        current_max = max(number, current_max * number)
        current_min = min(number, current_min * number)
        maximum_product = max(maximum_product, current_max)

    return maximum_product


if __name__ == "__main__":
    numbers = [2, 3, -2, 4]
    print(max_product_subarray(numbers))