
# alternate arrangement of positive and negative numbers in an array
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
pos = []
neg = []    

#seperate positive and negative numbers
for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

result = [0] * len(arr)
pos_index = 0
neg_index = 1
# fill the result array with alternate positive and negative numbers
for num in pos:
    if pos_index < len(arr):
        result[pos_index] = num
        pos_index += 2

for num in neg:
    if neg_index < len(arr):
        result[neg_index] = num
        neg_index += 2

print("Resultant array:", result)
