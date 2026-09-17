def count_passes_to_sort(array):
    """Return the number of bubble-sort passes needed to sort an array.

    A pass is counted only when it performs at least one swap. The input
    array is copied so that this function does not modify the caller's data.
    """
    values = array.copy()
    passes = 0

    for end in range(len(values) - 1, 0, -1):
        swapped = False

        for index in range(end):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
                swapped = True

        if not swapped:
            break

        passes += 1

    return passes


if __name__ == "__main__":
    array = [5, 1, 4, 2, 8]
    print("Number of passes:", count_passes_to_sort(array))
