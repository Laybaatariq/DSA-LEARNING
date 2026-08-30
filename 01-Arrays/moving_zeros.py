
# moving zeros to end by using two pointers
# i and pos

arr = [0,1,2,0,0,3,4]
pos=0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos+=1

while pos < len(arr):
     arr[pos]= 0
     pos+=1

print("Array After Moving all zeros to end:", arr)
      