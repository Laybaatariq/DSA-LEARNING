
# Implement Min Stack
#
# A Min Stack supports:
# push()    -> Insert an element
# pop()     -> Remove the top element
# top()     -> Get the top element
# get_min() -> Get the minimum element in O(1)


class MinStack:

    def __init__(self):

        # Stores all normal stack elements.
        self.stack = []

        # Stores minimum values at different stages.
        self.min_stack = []

    def push(self, value):

        # Insert the value into the normal stack.
        self.stack.append(value)

        # If min_stack is empty, this is the first element.
        # Otherwise, compare with the current minimum.
        if not self.min_stack or value <= self.min_stack[-1]:

            # Save the new minimum.
            self.min_stack.append(value)

        print(value, "pushed into stack")

    def pop(self):

        # Check whether the stack is empty.
        if not self.stack:
            print("Stack Underflow! Stack is empty")
            return None

        # Remove the top element from the normal stack.
        removed = self.stack.pop()

        # If removed element is also the current minimum,
        # remove it from min_stack as well.
        if removed == self.min_stack[-1]:
            self.min_stack.pop()

        print(removed, "popped from stack")
        return removed

    def top(self):

        # Return the top element without removing it.
        if not self.stack:
            print("Stack is empty")
            return None

        return self.stack[-1]

    def get_min(self):

        # The top of min_stack always stores
        # the current minimum value.
        if not self.min_stack:
            print("Stack is empty")
            return None

        return self.min_stack[-1]

    def display(self):

        print("Normal Stack:", self.stack)
        print("Minimum Stack:", self.min_stack)


# Create a Min Stack.
s = MinStack()

# Insert elements.
s.push(5)
s.push(3)
s.push(7)
s.push(2)
s.push(8)

# Display both stacks.
s.display()

# Get current minimum.
print("Minimum element:", s.get_min())

# Remove top element.
s.pop()

# Check minimum again.
print("Minimum after pop:", s.get_min())

# Remove another element.
s.pop()

# Check minimum again.
print("Current minimum:", s.get_min())

# Check top element.
print("Top element:", s.top())
