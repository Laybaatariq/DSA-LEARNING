def median_of_two_sorted_arrays(nums1, nums2):
    """Find the median of two sorted arrays."""
    merged = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    total = len(merged)
    mid = total // 2

    if total % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    return merged[mid]


if __name__ == "__main__":
    arr1 = [1, 3]
    arr2 = [2]
    print(median_of_two_sorted_arrays(arr1, arr2))
