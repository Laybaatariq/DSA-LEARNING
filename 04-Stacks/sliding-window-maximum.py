
# Sliding Window Maximum
# Using Deque

from collections import deque


def sliding_window_maximum(arr, k):

    # Deque stores indexes of useful elements.
    dq = deque()

    # Store maximum of every window.
    result = []

    for i in range(len(arr)):

        # Remove indexes outside the current window.
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from the back.
        # They cannot become maximum while current
        # element remains inside the window.
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        # Add current index.
        dq.append(i)

        # Start recording answers when first
        # complete window is formed.
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# Driver code
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print("Original Array:", arr)
print("Window Size:", k)
print("Sliding Window Maximum:",
      sliding_window_maximum(arr, k))

