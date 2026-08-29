
arr = [1,2,2,3,3,4,5]

result=[]
seen=[]

for i in arr:
    if i not in seen:
        result.append(i)
        seen.append(i)
print("Array after removing duplicates:",result)