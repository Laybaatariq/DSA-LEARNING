def kth_smallest(arr, k):
    """Return the kth smallest element in an array."""
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]


def kth_largest(arr, k):
    """Return the kth largest element in an array."""
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[k - 1]


if __name__ == "__main__":
    arr = [7, 2, 9, 1, 6, 8, 3]
    k = 3

    print("Kth smallest:", kth_smallest(arr, k))
    print("Kth largest:", kth_largest(arr, k))
