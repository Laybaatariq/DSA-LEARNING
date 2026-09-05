
def merge_without_extra_space(arr1, arr2):
    """Merge two sorted arrays in place without creating a third array."""
    if not arr2:
        return

    for index in range(len(arr1)):
        if arr1[index] > arr2[0]:
            arr1[index], arr2[0] = arr2[0], arr1[index]
            arr2.sort()


if __name__ == "__main__":
    arr1 = [1, 5, 9]
    arr2 = [2, 3, 4]

    merge_without_extra_space(arr1, arr2)

    print(arr1)
    print(arr2)