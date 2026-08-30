
# missing number by formula

arr=[3,4,6,7,8]
actual_sum=0
n = 5
expected_sum = n*(n+1)//2

for num in arr:
    actual_sum+=num

missing_num= expected_sum - actual_sum

print("The Missing Number is:", missing_num)


