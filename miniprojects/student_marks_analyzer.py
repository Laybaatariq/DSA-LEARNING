# ===== Student Marks Analyzer ======

arr = [85, 92, 78, 90,88]

def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest=num
            return largest

def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num
            return second

def reverse_array(arr):
    i = 0
    j = len(arr) -1

    for i in range(len(arr) -1):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1

    return arr

def is_sorted(arr):

    is_sorted = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break
    
    return is_sorted


print("Highest Marks:", find_largest(arr))
print("Second Highest",second_largest(arr))
print("Reverse Array:", reverse_array(arr))
print("Sorted or not:", is_sorted(arr))