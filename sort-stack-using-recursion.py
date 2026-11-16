
# Sort a Stack Using Recursion

def insert_sorted(stack, item):
    # Base case: Stack is empty OR
    # top element is smaller than or equal to item.
    if len(stack) == 0 or stack[-1] <= item:
        stack.append(item)
        return

    # Remove the top element.
    top = stack.pop()

    # Find the correct position recursively.
    insert_sorted(stack, item)

    # Restore the removed element.
    stack.append(top)


def sort_stack(stack):
    # Base case: Empty stack or single element.
    if len(stack) <= 1:
        return

    # Remove the top element.
    top = stack.pop()

    # Recursively sort remaining stack.
    sort_stack(stack)

    # Insert removed element in sorted position.
    insert_sorted(stack, top)


# Driver code
stack = [30, 10, 50, 20, 40]

print("Original Stack:", stack)

sort_stack(stack)

print("Sorted Stack:", stack)

