
# Reverse nodes of a linked list in groups of k

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_k_group(head, k):

    # If list is empty or k is 1, no reversal is needed
    if head is None or k <= 1:
        return head

    current = head
    count = 0

    # Check whether a complete group of k nodes exists
    while current is not None and count < k:
        current = current.next
        count += 1

    # Reverse only if we have exactly k nodes
    if count == k:

        previous = None
        current = head
        count = 0

        # Reverse the current group
        while current is not None and count < k:
            next_node = current.next

            current.next = previous
            previous = current
            current = next_node

            count += 1

        # Connect the original first node (now last)
        # to the next group's reversed result
        head.next = reverse_k_group(current, k)

        # Previous is the new head of this group
        return previous

    # Fewer than k nodes remain, so keep them unchanged
    return head


def print_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

k = 3

print("Original Linked List:")
print_list(head)

head = reverse_k_group(head, k)

print("After Reversing in Groups of", k)
print_list(head)

