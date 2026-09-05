
arr = [1,3,5,4,2]

# step 1: find pivot
i = len(arr) - 2
while i>=0 and arr[i] >= arr[i+1]:
    i-=1

# step 2: find element greater than pivot
if i>=0:
    j=len(arr) -1
    while arr[j] <= arr[i]:
        j-=1
    arr[i], arr[j] = arr[j], arr[i]

# step 3: reverse the suffix
arr[i+1:] = reversed(arr[i+1:])

print(arr)