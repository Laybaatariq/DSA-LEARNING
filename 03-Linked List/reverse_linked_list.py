"""Reverse a singly linked list by changing its links one at a time."""


class Node:
    """One item in a linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list(values):
    """Create a linked list from a regular Python list of values."""
    if len(values) == 0:
        return None

    head = Node(values[0])
    current_node = head

    for value in values[1:]:
        current_node.next = Node(value)
        current_node = current_node.next

    return head


def print_linked_list(head):
    """Print the values in the list from beginning to end."""
    current_node = head

    while current_node is not None:
        print(current_node.value, end="")

        if current_node.next is not None:
            print(" -> ", end="")

        current_node = current_node.next

    print()


def reverse_linked_list(head):
    """Reverse the links and return the new first node."""
    previous_node = None
    current_node = head

    while current_node is not None:
        # Save the next node before changing the link.
        next_node = current_node.next

        # Turn the current node's link around.
        current_node.next = previous_node

        # Move both pointers one step forward.
        previous_node = current_node
        current_node = next_node

    # The old last node is now the first node.
    return previous_node


numbers = [10, 20, 30, 40]
head = create_linked_list(numbers)

print("Original list:")
print_linked_list(head)

head = reverse_linked_list(head)

print("Reversed list:")
print_linked_list(head)
