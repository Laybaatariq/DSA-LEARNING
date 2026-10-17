
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_loop_start(head):
    slow = head
    fast = head

    # Step 1: Detect the loop
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None  # No loop exists

    # Step 2: Find the loop's starting node
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Create linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Create a loop: 50 -> 20
head.next.next.next.next.next = head.next

# Find the starting node
result = find_loop_start(head)

if result is not None:
    print("Loop starts at node:", result.data)
else:
    print("No loop exists")
