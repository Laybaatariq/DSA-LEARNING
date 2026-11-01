
# Reverse Alternate K Nodes in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Insert a node at the end
def insert(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


# Display linked list
def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Reverse alternate groups of k nodes
def reverse_alternate_k(head, k):

    # Invalid k or empty list
    if head is None or k <= 1:
        return head

    current = head
    previous = None

    # Controls whether the current group is reversed
    should_reverse = True

    while current:

        count = 0

        # Save the first node of the current group
        group_start = current

        if should_reverse:

            # Reverse k nodes
            previous = None

            while current and count < k:

                next_node = current.next

                current.next = previous

                previous = current
                current = next_node

                count += 1

            # Connect the previous part to the reversed group
            if head == group_start:
                head = previous
            else:
                previous_group_tail.next = previous

            # The original first node becomes the group tail
            group_start.next = current

            previous_group_tail = group_start

        else:

            # Skip k nodes without reversing them
            while current and count < k:

                previous_group_tail = current

                current = current.next

                count += 1

        # Toggle the operation for the next group
        should_reverse = not should_reverse

    return head


# Main program
head = None

values = [1, 2, 3, 4, 5, 6, 7, 8]

for value in values:
    head = insert(head, value)

k = 3

print("Original Linked List:")
display(head)

head = reverse_alternate_k(head, k)

print("After Reversing Alternate K Nodes:")
display(head)

