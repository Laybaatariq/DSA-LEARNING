
# sort 0s,1s and 2s (dutch national flag problem)
# three pointers

arr=[2,0,2,1,1,2]

low=0
mid=0
high= len(arr)-1

while mid<=high:
    if arr[mid] == 0:
        arr[low],arr[mid] = arr[mid],arr[low]
        low+=1
        mid+=1
    elif arr[mid] == 1:
        mid+=1
    else:
        arr[mid],arr[high] = arr[high],arr[mid]
        high-=1
print ("Sorted 0s,1s,2s:", arr)

