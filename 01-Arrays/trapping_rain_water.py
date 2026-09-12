
height = [0,1,0,2,1,0,1,3,2,1,2,1]
water = 0

for i in range(len(height)):
    left_max = max(height[:i+1])
    right_max = max(height[i:])

    water_level = min(left_max, right_max)
    trapped= water_level-height[i]
    water += trapped

print("Trapped water:", water)