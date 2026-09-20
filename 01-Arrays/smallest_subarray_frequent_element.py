from collections import Counter


def smallest_subarray_with_frequent_element(array):
    """Return the most frequent element and the shortest subarray containing it."""
    if not array:
        return None, []

    frequencies = Counter(array)
    highest_frequency = max(frequencies.values())
    frequent_elements = {
        element
        for element, frequency in frequencies.items()
        if frequency == highest_frequency
    }

    best_start = 0
    best_end = len(array)
    frequent_element = None

    for element in array:
        if element not in frequent_elements:
            continue

        start = array.index(element)
        end = len(array) - 1 - array[::-1].index(element)

        if end - start < best_end - best_start:
            best_start = start
            best_end = end + 1
            frequent_element = element

    return frequent_element, array[best_start:best_end]


array = [1, 2, 2, 3, 1, 4, 2, 1]
element, subarray = smallest_subarray_with_frequent_element(array)

print("Most frequent element:", element)
print("Smallest subarray:", subarray)
