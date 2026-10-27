"""Find the node shared by two singly linked lists."""


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


def get_length_and_tail(head):
    """Return how many nodes are in the list and its last node."""
    length = 0
    current_node = head
    last_node = None

    while current_node is not None:
        length += 1
        last_node = current_node
        current_node = current_node.next

    return length, last_node


def find_intersection_node(first_head, second_head):
    """Return the shared node, or None if the lists do not intersect.

    Two lists intersect only when they share the same node object.
    Nodes with equal values are not enough.
    """
    first_length, first_tail = get_length_and_tail(first_head)
    second_length, second_tail = get_length_and_tail(second_head)

    # Intersecting lists must finish at the same exact node.
    if first_tail is not second_tail:
        return None

    # Start both pointers the same distance from the end.
    while first_length > second_length:
        first_head = first_head.next
        first_length -= 1

    while second_length > first_length:
        second_head = second_head.next
        second_length -= 1

    # Walk together. The first node object they share is the intersection.
    while first_head is not second_head:
        first_head = first_head.next
        second_head = second_head.next

    return first_head


def print_linked_list(head):
    """Print a linked list from its first node to its last."""
    current_node = head

    while current_node is not None:
        print(current_node.value, end="")

        if current_node.next is not None:
            print(" -> ", end="")

        current_node = current_node.next

    print()


if __name__ == "__main__":
    # These two lists have separate beginnings but share the same last nodes.
    first_head = create_linked_list([1, 2, 3])
    second_head = create_linked_list([9, 8])
    shared_part = create_linked_list([7, 6])

    first_tail = first_head
    while first_tail.next is not None:
        first_tail = first_tail.next
    first_tail.next = shared_part

    second_tail = second_head
    while second_tail.next is not None:
        second_tail = second_tail.next
    second_tail.next = shared_part

    print("First linked list:")
    print_linked_list(first_head)
    print("Second linked list:")
    print_linked_list(second_head)

    intersection = find_intersection_node(first_head, second_head)

    if intersection is None:
        print("The lists do not intersect.")
    else:
        print(f"The lists intersect at the node with value {intersection.value}.")
