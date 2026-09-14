
arr= [1,4,45,6,10,8]
target = 22

arr.sort()

found= False

for i in range(len(arr) -2):
    left = i+1
    right= len(arr) -1
    while left < right:
        total = arr[i] + arr[left] + arr[right]
        if total == target:
            found = True
            break
        elif total < target:
            left += 1
        else:
            right -= 1

if found:
    print("Triplet found")
else:
    print("Triplet not found")