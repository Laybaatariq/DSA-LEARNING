
# Implement Stack Using Linked List
# Stack follows LIFO: Last In, First Out.


# Node class represents one element of the linked list.
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        # Initially stack is empty.
        # Top points to the first node.
        self.top = None

    def is_empty(self):
        # If top is None, stack contains no nodes.
        return self.top is None

    def push(self, value):

        # Create a new node.
        new_node = Node(value)

        # New node points to the current top node.
        new_node.next = self.top

        # Update top to the new node.
        # Now the new node becomes the stack's top.
        self.top = new_node

        print(value, "pushed into stack")

    def pop(self):

        # Check whether stack is empty.
        if self.is_empty():
            print("Stack Underflow! Stack is empty")
            return None

        # Store the top node's value before removing it.
        removed_value = self.top.data

        # Move top to the next node.
        # This removes the previous top from the stack.
        self.top = self.top.next

        print(removed_value, "popped from stack")

        return removed_value

    def peek(self):

        # Return the top value without removing the node.
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.top.data

    def display(self):

        # Start traversal from the top node.
        current = self.top

        if current is None:
            print("Stack is empty")
            return

        print("Stack (top to bottom):", end=" ")

        # Visit each node until the end of the linked list.
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create an empty stack.
s = Stack()

# Insert elements into the stack.
s.push(10)
s.push(20)
s.push(30)

# Display stack elements.
s.display()

# Check the top element.
print("Top element:", s.peek())

# Remove the top element.
s.pop()

# Display the updated stack.
s.display()
