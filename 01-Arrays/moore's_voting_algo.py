

# find the majority element
# find the length and use n/2 to check the appearance of number in an array

arr=[2,2,1,1,1,2,2]

candidate=None
count=0

for num in arr:
    if count==0:
        candidate=num
    if num == candidate:
        count+=1
    else:
        count-=1

if arr.count(candidate) > len(arr) // 2:
    print("Majority Element is:", candidate)
else:
    print("No majority element found")