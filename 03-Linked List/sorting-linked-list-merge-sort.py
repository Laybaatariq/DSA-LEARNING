
# Sorting a Linked List Using Merge Sort

# Node class represents one node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert a new node at the end
def insert(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


# Function to display the linked list
def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Step 1: Find the middle node using slow and fast pointers
def get_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Step 2: Merge two sorted linked lists
def merge(left, right):

    # Dummy node makes merging easier
    dummy = Node(0)
    tail = dummy

    while left and right:

        # Select the smaller value
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next

        tail = tail.next

    # Attach remaining nodes
    if left:
        tail.next = left
    else:
        tail.next = right

    return dummy.next


# Step 3: Apply Merge Sort recursively
def merge_sort(head):

    # Base case: empty list or single node
    if head is None or head.next is None:
        return head

    # Divide the list into two halves
    middle = get_middle(head)

    right_half = middle.next

    # Break the connection between halves
    middle.next = None

    # Recursively sort both halves
    left = merge_sort(head)
    right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left, right)


# Main program
head = None

values = [40, 10, 30, 20, 50]

for value in values:
    head = insert(head, value)

print("Original Linked List:")
display(head)

head = merge_sort(head)

print("Sorted Linked List:")
display(head)

