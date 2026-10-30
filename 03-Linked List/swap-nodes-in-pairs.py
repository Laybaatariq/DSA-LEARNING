
# Swap Nodes in Pairs in a Linked List

# Node class represents one node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Insert a new node at the end
def insert(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


# Display the linked list
def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Swap adjacent nodes in pairs
def swap_pairs(head):

    # Dummy node helps handle swapping from the first node
    dummy = Node(0)
    dummy.next = head

    previous = dummy

    while previous.next and previous.next.next:

        # Identify the two nodes to swap
        first = previous.next
        second = first.next

        # Change links to swap nodes
        first.next = second.next
        second.next = first
        previous.next = second

        # Move previous forward for the next pair
        previous = first

    return dummy.next


# Main program
head = None

values = [10, 20, 30, 40, 50]

for value in values:
    head = insert(head, value)

print("Original Linked List:")
display(head)

head = swap_pairs(head)

print("After Swapping Pairs:")
display(head)

