"""Check whether a singly linked list reads the same in both directions."""


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
    """Reverse a list in place and return its new first node."""
    previous_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


def is_palindrome(head):
    """Return whether the list is a palindrome, restoring its original links."""
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # For an odd-length list, skip its middle node.
    if fast_pointer is not None:
        slow_pointer = slow_pointer.next

    reversed_second_half = reverse_linked_list(slow_pointer)
    first_half_node = head
    second_half_node = reversed_second_half
    palindrome = True

    while second_half_node is not None:
        if first_half_node.value != second_half_node.value:
            palindrome = False
            break

        first_half_node = first_half_node.next
        second_half_node = second_half_node.next

    # Restore the list so this check does not leave its links changed.
    reverse_linked_list(reversed_second_half)

    return palindrome


head = create_linked_list([1, 2, 3, 2, 1])

print("Linked list:")
print_linked_list(head)
print(f"Is palindrome: {is_palindrome(head)}")