
# Segregate Even and Odd Nodes in a Linked List

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


# Display the linked list
def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Segregate even and odd nodes
def segregate_even_odd(head):

    # Empty list or single node needs no changes
    if head is None or head.next is None:
        return head

    # Heads and tails of even and odd lists
    even_head = None
    even_tail = None

    odd_head = None
    odd_tail = None

    current = head

    while current:

        # Save the next node before changing links
        next_node = current.next

        # Detach current node from the original list
        current.next = None

        # Check whether the current value is even
        if current.data % 2 == 0:

            # First even node
            if even_head is None:
                even_head = current
                even_tail = current

            else:
                even_tail.next = current
                even_tail = current

        else:

            # First odd node
            if odd_head is None:
                odd_head = current
                odd_tail = current

            else:
                odd_tail.next = current
                odd_tail = current

        # Move to the next original node
        current = next_node

    # If there are no even nodes, return the odd list
    if even_head is None:
        return odd_head

    # Connect even list to odd list
    even_tail.next = odd_head

    # Return the head of the combined list
    return even_head


# Main program
head = None

values = [17, 15, 8, 12, 10, 5, 4]

for value in values:
    head = insert(head, value)

print("Original Linked List:")
display(head)

head = segregate_even_odd(head)

print("After Even-Odd Segregation:")
display(head)

