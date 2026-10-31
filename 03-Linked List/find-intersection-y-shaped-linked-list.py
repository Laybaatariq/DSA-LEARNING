
# Find Intersection of Y-Shaped Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Find the intersection using two pointers
def find_intersection(head1, head2):

    # Start both pointers at the heads of their lists
    pointer1 = head1
    pointer2 = head2

    # Continue until both pointers meet
    while pointer1 != pointer2:

        # If pointer reaches the end, switch to the other list
        if pointer1 is None:
            pointer1 = head2
        else:
            pointer1 = pointer1.next

        if pointer2 is None:
            pointer2 = head1
        else:
            pointer2 = pointer2.next

    # They meet at the intersection node,
    # or both become None if there is no intersection
    return pointer1


# Display a linked list
def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create the common part of the Y-shaped list
common = Node(30)
common.next = Node(40)
common.next.next = Node(50)


# Create first linked list
head1 = Node(10)
head1.next = Node(20)
head1.next.next = common


# Create second linked list
head2 = Node(15)
head2.next = common


print("First Linked List:")
display(head1)

print("Second Linked List:")
display(head2)


# Find the intersection
intersection = find_intersection(head1, head2)

if intersection:
    print("Intersection Node:", intersection.data)
else:
    print("No Intersection Found")

