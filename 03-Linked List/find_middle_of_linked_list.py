"""Find the middle node of a singly linked list."""


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


def find_middle_node(head):
    """Return the middle node; for an even list, return the second middle."""
    slow_pointer = head
    fast_pointer = head

    # The fast pointer moves twice as quickly as the slow pointer.
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # When the fast pointer reaches the end, the slow one is in the middle.
    return slow_pointer


numbers = [10, 20, 30, 40, 50, 60]
head = create_linked_list(numbers)

print("Linked list:")
print_linked_list(head)

middle_node = find_middle_node(head)

if middle_node is None:
    print("The list is empty, so it has no middle node.")
else:
    print(f"Middle node: {middle_node.value}")
