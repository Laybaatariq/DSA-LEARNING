
# find subarray with a given sun
# using two pointers and variable current_sum

arr =[1,2,3,7,5]

target=12

left=0
current_sum=0

for right in range(len(arr)):
    current_sum+=arr[right] 

    while current_sum > target:
        current_sum -= arr[left]
        left+=1

    if current_sum == target:
       print("Subarray Found!")
       print(arr[left:right+1])  
       break

    