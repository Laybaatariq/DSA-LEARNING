
# Implement Stack Using Array
# Stack follows LIFO: Last In, First Out.


class Stack:

    def __init__(self, capacity):
        # Create an empty array with a fixed capacity.
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        # Stack is empty if it contains no elements.
        return len(self.stack) == 0

    def is_full(self):
        # Stack is full when it reaches its capacity.
        return len(self.stack) == self.capacity

    def push(self, value):
        # Check overflow before inserting a new element.
        if self.is_full():
            print("Stack Overflow! Cannot insert", value)
            return

        # Add the new element at the top of the stack.
        self.stack.append(value)
        print(value, "pushed into stack")

    def pop(self):
        # Cannot remove an element from an empty stack.
        if self.is_empty():
            print("Stack Underflow! Stack is empty")
            return None

        # Remove and return the last inserted element.
        removed = self.stack.pop()
        print(removed, "popped from stack")
        return removed

    def peek(self):
        # Return the top element without removing it.
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.stack[-1]

    def display(self):
        # Display elements from bottom to top.
        if self.is_empty():
            print("Stack is empty")
            return

        print("Stack (bottom to top):", self.stack)


# Create a stack with capacity 5.
s = Stack(5)

# Insert elements.
s.push(10)
s.push(20)
s.push(30)

# Display the stack.
s.display()

# Check the top element.
print("Top element:", s.peek())

# Remove an element.
s.pop()

# Display the updated stack.
s.display()
