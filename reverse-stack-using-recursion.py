
# Reverse a Stack Using Recursion

def insert_at_bottom(stack, item):
    # Base case: If stack is empty,
    # insert the item at the bottom.
    if len(stack) == 0:
        stack.append(item)
        return

    # Remove the top element temporarily.
    top = stack.pop()

    # Recursively reach the bottom.
    insert_at_bottom(stack, item)

    # Restore the removed element.
    stack.append(top)


def reverse_stack(stack):
    # Base case: Empty stack or single element.
    if len(stack) <= 1:
        return

    # Remove the top element.
    top = stack.pop()

    # Reverse the remaining stack.
    reverse_stack(stack)

    # Insert the removed element at the bottom.
    insert_at_bottom(stack, top)


# Driver code
stack = [1, 2, 3, 4, 5]

print("Original Stack:", stack)

reverse_stack(stack)

print("Reversed Stack:", stack)

