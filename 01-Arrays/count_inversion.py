
# count inversion in an array

arr= [2,4,1,3,5]
count=0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]>arr[j]:
            count+=1
print("Number of Inversions are:", count)
