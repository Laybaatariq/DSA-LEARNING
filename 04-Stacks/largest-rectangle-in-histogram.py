
# Largest Rectangle in Histogram
# Using Monotonic Increasing Stack

def largest_rectangle(heights):

    # Stack stores indexes of histogram bars.
    stack = []

    # Maximum rectangle area found so far.
    max_area = 0

    # Add a zero-height bar at the end.
    # This forces all remaining bars to be processed.
    arr = heights + [0]

    for i in range(len(arr)):

        # If current bar is smaller than stack top,
        # calculate the rectangle for the popped bar.
        while stack and arr[i] < arr[stack[-1]]:

            # Remove the bar whose rectangle is calculated.
            height = arr[stack.pop()]

            # Calculate rectangle width.
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            # Calculate rectangle area.
            area = height * width

            # Update maximum area.
            max_area = max(max_area, area)

        # Store current index.
        stack.append(i)

    return max_area


# Driver code
heights = [2, 1, 5, 6, 2, 3]

print("Histogram:", heights)
print("Largest Rectangle Area:", largest_rectangle(heights))

