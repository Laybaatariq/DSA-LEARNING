"""Merge two sorted singly linked lists into one sorted linked list."""


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


def merge_two_sorted_lists(first_head, second_head):
    """Merge sorted lists by reusing their nodes and return the merged head."""
    merged_head = Node(None)
    tail = merged_head
    first_node = first_head
    second_node = second_head

    while first_node is not None and second_node is not None:
        if first_node.value <= second_node.value:
            tail.next = first_node
            first_node = first_node.next
        else:
            tail.next = second_node
            second_node = second_node.next

        tail = tail.next

    # Append whichever list still has nodes.
    tail.next = first_node if first_node is not None else second_node

    return merged_head.next


first_list = create_linked_list([1, 3, 5, 7])
second_list = create_linked_list([2, 4, 6, 8])

print("First sorted list:")
print_linked_list(first_list)

print("Second sorted list:")
print_linked_list(second_list)

merged_list = merge_two_sorted_lists(first_list, second_list)

print("Merged sorted list:")
print_linked_list(merged_list)