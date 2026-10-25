"""Detect a loop in a linked list and remove it."""


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
    """Print the values in a list after confirming it has no loop."""
    current_node = head

    while current_node is not None:
        print(current_node.value, end="")

        if current_node.next is not None:
            print(" -> ", end="")

        current_node = current_node.next

    print()


def detect_and_remove_loop(head):
    """Remove a loop if one exists, and return True when a loop was removed."""
    slow_pointer = head
    fast_pointer = head
    meeting_node = None

    # The slow pointer takes one step and the fast pointer takes two.
    # If they meet, the list has a loop.
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer is fast_pointer:
            meeting_node = slow_pointer
            break

    if meeting_node is None:
        return False

    # Move one pointer to the head. Moving both one step at a time
    # makes them meet at the first node that belongs to the loop.
    loop_start = head
    while loop_start is not meeting_node:
        loop_start = loop_start.next
        meeting_node = meeting_node.next

    # Walk around the loop until we find the node that points back
    # to its start, then cut that link.
    last_node_in_loop = loop_start
    while last_node_in_loop.next is not loop_start:
        last_node_in_loop = last_node_in_loop.next

    last_node_in_loop.next = None
    return True


if __name__ == "__main__":
    head = create_linked_list([10, 20, 30, 40, 50])

    # Create a loop for this example: the last node points back to 30.
    third_node = head.next.next
    last_node = head
    while last_node.next is not None:
        last_node = last_node.next
    last_node.next = third_node

    if detect_and_remove_loop(head):
        print("A loop was found and removed.")
    else:
        print("No loop was found.")

    print("List after checking:")
    print_linked_list(head)
