"""Remove repeated values from a sorted singly linked list."""


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
    current_node = head

    while current_node is not None and current_node.next is not None:
        if current_node.value == current_node.next.value:
            # Equal values are next to each other in a sorted list.
            # Bypass the duplicate node; keep checking this position in case
            # there are more copies of the same value.
            current_node.next = current_node.next.next
        else:
            # Move on only after the next node has a different value.
            current_node = current_node.next

    return head


head = create_linked_list([1, 1, 2, 3, 3, 3, 4, 5, 5])

print("Sorted list with duplicates:")
print_linked_list(head)

head = remove_duplicates(head)

print("Sorted list after removing duplicates:")
print_linked_list(head)
