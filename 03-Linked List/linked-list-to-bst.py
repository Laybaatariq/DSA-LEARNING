
# Convert a sorted linked list into a height-balanced BST

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sorted_list_to_bst(head):

    # Base case: empty linked list
    if head is None:
        return None

    # If only one node exists, it becomes the tree node
    if head.next is None:
        return TreeNode(head.data)

    # Find the middle node using slow and fast pointers
    slow = head
    fast = head
    previous = None

    while fast is not None and fast.next is not None:
        previous = slow
        slow = slow.next
        fast = fast.next.next

    # Break the linked list into two halves
    previous.next = None

    # Middle node becomes the root
    root = TreeNode(slow.data)

    # Build left subtree from the first half
    root.left = sorted_list_to_bst(head)

    # Build right subtree from nodes after the middle
    root.right = sorted_list_to_bst(slow.next)

    return root


# Print the BST using preorder traversal
def preorder(root):

    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Create sorted linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

# Convert linked list into BST
root = sorted_list_to_bst(head)

print("BST Preorder Traversal:")
preorder(root)
print()

