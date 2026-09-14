
arr = [100, 4, 200, 1, 3, 2]

numbers = set(arr)
longest_streak = 0

for num in numbers:
    if num - 1 not in numbers:
        current_num = num
        current_streak = 1

        while current_num + 1 in numbers:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

print(longest_streak)