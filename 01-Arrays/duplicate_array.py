
arr = [1,3,4,2,2]

seen = set()

for num in arr:
    if num in seen:
        print(num)
        break
    seen.add(num)
        
