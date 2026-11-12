
# Implement Queue Using Linked List
# Queue follows FIFO: First In, First Out.


# Node class represents one queue element.
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        # Initially queue is empty.
        self.front = None
        self.rear = None

    def is_empty(self):
        # Queue is empty when front is None.
        return self.front is None

    def enqueue(self, value):

        # Create a new node.
        new_node = Node(value)

        # If queue is empty, both front and rear
        # must point to the newly created node.
        if self.is_empty():
            self.front = new_node
            self.rear = new_node

        else:
            # Connect the current rear to the new node.
            self.rear.next = new_node

            # Update rear to the newly inserted node.
            self.rear = new_node

        print(value, "inserted into queue")

    def dequeue(self):

        # Cannot remove an element from an empty queue.
        if self.is_empty():
            print("Queue Underflow! Queue is empty")
            return None

        # Store the front value before removing it.
        removed_value = self.front.data

        # Move front to the next node.
        self.front = self.front.next

        # If the queue becomes empty after deletion,
        # rear must also become None.
        if self.front is None:
            self.rear = None

        print(removed_value, "removed from queue")

        return removed_value

    def peek(self):

        # Return the front value without removing it.
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.front.data

    def display(self):

        # Start traversal from the front node.
        current = self.front

        if current is None:
            print("Queue is empty")
            return

        print("Queue (front to rear):", end=" ")

        # Visit every node until the end.
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create an empty queue.
q = Queue()

# Insert elements at the rear.
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Display queue elements.
q.display()

# Check the front element.
print("Front element:", q.peek())

# Remove the front element.
q.dequeue()

# Display updated queue.
q.display()

# Insert another element.
q.enqueue(40)

q.display()
