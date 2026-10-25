"""Reverse a linked list by using a stack to remember its nodes."""


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


def reverse_linked_list_using_stack(head):
    """Reverse the list and return its new first node."""
    node_stack = []
    current_node = head

    # Put each node on the stack. The last node will be on top.
    while current_node is not None:
        node_stack.append(current_node)
        current_node = current_node.next

    if len(node_stack) == 0:
        return None

    # Take the last node first; it becomes the new head.
    new_head = node_stack.pop()
    new_head.next = None
    current_node = new_head

    # Pop the remaining nodes and connect them in reverse order.
    while len(node_stack) > 0:
        previous_node = node_stack.pop()
        current_node.next = previous_node
        current_node = previous_node
        current_node.next = None

    return new_head


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    head = create_linked_list(numbers)

    print("Original list:")
    print_linked_list(head)

    head = reverse_linked_list_using_stack(head)

    print("Reversed list:")
    print_linked_list(head)
