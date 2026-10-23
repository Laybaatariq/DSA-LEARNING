"""Remove repeated values from an unsorted singly linked list."""


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


def remove_duplicates(head):
    """Remove repeated values, keeping the first node for each value."""
    seen_values = set()
    current_node = head
    previous_node = None

    while current_node is not None:
        if current_node.value in seen_values:
            # Link around the repeated node so it is no longer in the list.
            previous_node.next = current_node.next
        else:
            # Remember each value the first time it appears.
            seen_values.add(current_node.value)
            previous_node = current_node

        # Advance to the next node that remains in the list.
        current_node = current_node.next

    return head


head = create_linked_list([4, 2, 4, 3, 2, 1, 3, 5, 1])

print("Unsorted list with duplicates:")
print_linked_list(head)

head = remove_duplicates(head)

print("Unsorted list after removing duplicates:")
print_linked_list(head)
