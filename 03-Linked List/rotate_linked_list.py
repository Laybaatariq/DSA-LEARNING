"""Rotate a singly linked list to the right by k positions."""


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


def rotate_linked_list(head, steps):
    """Move the last `steps` nodes to the beginning of the list."""
    if steps < 0:
        raise ValueError("The number of rotation steps cannot be negative.")

    # An empty list or a list with one node cannot change when rotated.
    if head is None or head.next is None or steps == 0:
        return head

    # Count the nodes and remember the current last node.
    list_length = 1
    last_node = head

    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    # Rotating by the list's full length brings it back to the same order.
    steps = steps % list_length
    if steps == 0:
        return head

    # Temporarily connect the last node to the first to make a circle.
    last_node.next = head

    # The new last node is this many steps from the old head.
    steps_to_new_last = list_length - steps - 1
    new_last_node = head

    for _ in range(steps_to_new_last):
        new_last_node = new_last_node.next

    # Break the circle to finish the rotation.
    new_head = new_last_node.next
    new_last_node.next = None

    return new_head


if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5])

    print("Original list:")
    print_linked_list(head)

    head = rotate_linked_list(head, 2)

    print("List after rotating right by 2:")
    print_linked_list(head)
