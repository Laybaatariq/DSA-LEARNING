
# Implement Queue Using Two Stacks
# Queue follows FIFO: First In, First Out.


class Queue:

    def __init__(self):
        # Stack 1 stores newly inserted elements.
        self.stack1 = []

        # Stack 2 helps remove elements in FIFO order.
        self.stack2 = []

    def enqueue(self, value):
        # Insert the new element into stack1.
        # Python append() adds an element to the top.
        self.stack1.append(value)

        print(value, "inserted into queue")

    def dequeue(self):

        # If both stacks are empty, queue is empty.
        if not self.stack1 and not self.stack2:
            print("Queue is empty! Cannot dequeue")
            return None

        # Transfer elements only when stack2 is empty.
        # This avoids unnecessary transfers.
        if not self.stack2:

            # Move all elements from stack1 to stack2.
            while self.stack1:
                value = self.stack1.pop()
                self.stack2.append(value)

        # The oldest element is now at the top of stack2.
        removed = self.stack2.pop()

        print(removed, "removed from queue")
        return removed

    def peek(self):

        # If stack2 has elements, its top is the front.
        if self.stack2:
            return self.stack2[-1]

        # If stack2 is empty, stack1's bottom is the front.
        if self.stack1:
            return self.stack1[0]

        print("Queue is empty")
        return None

    def is_empty(self):
        # Queue is empty only if both stacks are empty.
        return not self.stack1 and not self.stack2

    def display(self):
        # stack2 must be displayed in reverse order,
        # because its top element is the queue front.
        queue_elements = (
            self.stack2[::-1] + self.stack1
        )

        if not queue_elements:
            print("Queue is empty")
        else:
            print("Queue (front to rear):", queue_elements)


# Create a queue.
q = Queue()

# Insert elements into the queue.
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Display queue.
q.display()

# Check the front element.
print("Front element:", q.peek())

# Remove the oldest element.
q.dequeue()

# Display updated queue.
q.display()

# Insert another element.
q.enqueue(40)

q.display()
