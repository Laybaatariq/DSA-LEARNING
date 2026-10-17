
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_loop(head):
    slow = head
    fast = head

    # Step 1: Detect the loop
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return head  # No loop exists

    # Step 2: Find the starting node of the loop
    slow = head

    if slow == fast:
        # Special case: loop starts at the head
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

    # Step 3: Remove the loop
    fast.next = None

    return head


def print_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Create a loop: 5 -> 3
head.next.next.next.next.next = head.next.next

delete_loop(head)

print("Linked list after deleting loop:")
print_list(head)
