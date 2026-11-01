
# Reorder Linked List
# Pattern: L0 -> Ln -> L1 -> Ln-1 -> ...

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Insert a node at the end
def insert(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


# Display linked list
def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Find the middle node
def find_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Reverse a linked list
def reverse(head):
    previous = None
    current = head

    while current:
        next_node = current.next

        current.next = previous

        previous = current
        current = next_node

    return previous


# Reorder the linked list
def reorder_list(head):

    # Empty or single-node list needs no changes
    if head is None or head.next is None:
        return head

    # Step 1: Find the middle
    middle = find_middle(head)

    # Step 2: Split the list into two halves
    second_half = middle.next
    middle.next = None

    # Step 3: Reverse the second half
    second_half = reverse(second_half)

    # Step 4: Merge both halves alternately
    first = head
    second = second_half

    while second:

        # Save next nodes before changing links
        first_next = first.next
        second_next = second.next

        # Connect first node to second node
        first.next = second

        # Connect second node to next first-half node
        second.next = first_next

        # Move both pointers forward
        first = first_next
        second = second_next

    return head


# Main program
head = None

values = [1, 2, 3, 4, 5]

for value in values:
    head = insert(head, value)

print("Original Linked List:")
display(head)

head = reorder_list(head)

print("Reordered Linked List:")
display(head)

