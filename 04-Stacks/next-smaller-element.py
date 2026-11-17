
# Next Smaller Element using Stack

def next_smaller_element(arr):
    n = len(arr)

    # Store answers for every element.
    result = [-1] * n

    # Stack stores indexes of unresolved elements.
    stack = []

    for i in range(n):

        # Find smaller elements for previous indexes.
        while stack and arr[i] < arr[stack[-1]]:

            # Remove the index whose answer is found.
            index = stack.pop()

            # Current element is its next smaller element.
            result[index] = arr[i]

        # Store current index for future comparison.
        stack.append(i)

    return result


# Driver code
arr = [4, 5, 2, 10, 8]

print("Original Array:", arr)
print("Next Smaller:", next_smaller_element(arr))
