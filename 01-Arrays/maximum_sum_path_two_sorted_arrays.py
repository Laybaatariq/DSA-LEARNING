def maximum_sum_path(first_array, second_array):
    """Return the maximum-sum path through two sorted arrays.

    At a common value, the path may switch from one array to the other.
    """
    first_index = 0
    second_index = 0
    first_sum = 0
    second_sum = 0
    maximum_sum = 0

    while first_index < len(first_array) and second_index < len(second_array):
        if first_array[first_index] < second_array[second_index]:
            first_sum += first_array[first_index]
            first_index += 1
        elif first_array[first_index] > second_array[second_index]:
            second_sum += second_array[second_index]
            second_index += 1
        else:
            maximum_sum += max(first_sum, second_sum) + first_array[first_index]
            first_sum = 0
            second_sum = 0
            first_index += 1
            second_index += 1

    while first_index < len(first_array):
        first_sum += first_array[first_index]
        first_index += 1

    while second_index < len(second_array):
        second_sum += second_array[second_index]
        second_index += 1

    return maximum_sum + max(first_sum, second_sum)


first_array = [2, 3, 7, 10, 12]
second_array = [1, 5, 7, 8, 10]

print("Maximum sum path:", maximum_sum_path(first_array, second_array))