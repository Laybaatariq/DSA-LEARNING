def find_pair_given_difference(numbers, difference):
    """Return the first pair with the given absolute difference, or None."""
    difference = abs(difference)
    seen = set()

    for number in numbers:
        if number - difference in seen:
            return number - difference, number
        if number + difference in seen:
            return number + difference, number
        seen.add(number)

    return None


if __name__ == "__main__":
    numbers = [5, 20, 3, 2, 50, 80]
    difference = 78
    print(find_pair_given_difference(numbers, difference))