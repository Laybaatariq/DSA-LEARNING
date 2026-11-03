# Partition a linked list around a given value x
# Smaller values come first; values >= x come after them.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def partition_list(head, x):
    # Dummy nodes make it easier to build both lists
    smaller_dummy = Node(0)
    greater_dummy = Node(0)

    # Tails point to the last nodes of both lists
    smaller_tail = smaller_dummy
    greater_tail = greater_dummy

    current = head

    while current is not None:
        # Save the next node before separating current
        next_node = current.next

        # Detach current node from the original list
        current.next = None

        if current.data < x:
            # Add node to the smaller-than-x list
            smaller_tail.next = current
            smaller_tail = current
        else:
            # Add node to the >= x list
            greater_tail.next = current
            greater_tail = current

        # Move to the next original node
        current = next_node

    # Join smaller list with the >= x list
    smaller_tail.next = greater_dummy.next

    # Return the start of the partitioned list
    return smaller_dummy.next


def print_list(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create linked list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
head = Node(3)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(5)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

x = 5

print("Before partition:")
print_list(head)

head = partition_list(head, x)

print("After partition around", x, ":")
print_list(head)
