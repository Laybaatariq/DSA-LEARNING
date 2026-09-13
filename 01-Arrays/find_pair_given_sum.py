def find_pair_given_sum(numbers, target):
    """Return the first pair whose values add up to target, or None."""
    seen = set()

    for number in numbers:
        complement = target - number
        if complement in seen:
            return complement, number
        seen.add(number)

    return None


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(find_pair_given_sum(numbers, target))
