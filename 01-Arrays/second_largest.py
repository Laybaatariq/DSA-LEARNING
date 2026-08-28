# Second largest number in an array

arr = [12, 35,1,10,34,6]

second_largest = float ('-inf')
largest = float ('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("the second largest is:",second_largest)