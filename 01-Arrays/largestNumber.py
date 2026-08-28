
# largest number

arr =[7,2,9,4,1]

largest = arr[0]

for i in range(1,len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
