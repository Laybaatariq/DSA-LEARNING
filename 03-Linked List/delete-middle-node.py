# Delete the middle node of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_middle(head):
    # Empty list ya sirf one node ho to result empty
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    previous = None

    # Fast pointer 2 steps aur slow pointer 1 step move karega
    while fast is not None and fast.next is not None:
        previous = slow
        slow = slow.next
        fast = fast.next.next

    # Slow ab middle node par hai
    # Previous ko middle ke next node se connect kar do
    previous.next = slow.next

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

print("Before deletion:")
print_list(head)

head = delete_middle(head)

print("After deletion:")
print_list(head)
