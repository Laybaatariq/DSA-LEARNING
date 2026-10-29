"""Merge k sorted linked lists into one sorted linked list."""


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
    """Combine two sorted lists by repeatedly choosing the smaller node."""
    answer_head = Node(0)
    answer_tail = answer_head

    while first_head is not None and second_head is not None:
        if first_head.value <= second_head.value:
            # The first list has the smaller next value, so use that node.
            answer_tail.next = first_head
            first_head = first_head.next
        else:
            # Otherwise, take the smaller node from the second list.
            answer_tail.next = second_head
            second_head = second_head.next

        answer_tail = answer_tail.next

    # One list may still have nodes left. They are already sorted.
    if first_head is not None:
        answer_tail.next = first_head
    else:
        answer_tail.next = second_head

    return answer_head.next


def merge_k_sorted_lists(list_heads):
    """Merge sorted, node-disjoint lists using pair-by-pair rounds."""
    current_lists = list(list_heads)

    if len(current_lists) == 0:
        return None

    # Merge pairs, then merge those results in the next round.
    # This keeps the work balanced instead of merging every list into
    # one growing list from left to right.
    while len(current_lists) > 1:
        merged_lists = []

        for index in range(0, len(current_lists), 2):
            first_head = current_lists[index]

            if index + 1 < len(current_lists):
                second_head = current_lists[index + 1]
            else:
                # If there is an unpaired list, carry it to the next round.
                second_head = None

            merged_head = merge_two_sorted_lists(first_head, second_head)
            merged_lists.append(merged_head)

        current_lists = merged_lists

    return current_lists[0]


if __name__ == "__main__":
    list_heads = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6]),
    ]

    print("Input lists:")
    for list_head in list_heads:
        print_linked_list(list_head)

    merged_head = merge_k_sorted_lists(list_heads)

    print("All lists merged in sorted order:")
    print_linked_list(merged_head)
