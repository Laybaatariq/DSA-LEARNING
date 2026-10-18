
def delete_node(next_node, head, value):
    # If the list is empty
    if head is None:
        return head

    # If the first node needs to be deleted
    if head == value:
        return next_node[head]

    current = head

    # Find the node before the node to delete
    while current is not None:
        next_value = next_node[current]

        if next_value == value:
            # Skip the node we want to delete
            next_node[current] = next_node[value]
            next_node.pop(value)
            return head

        current = next_value

    return head


def print_list(next_node, head):
    current = head

    while current is not None:
        print(current, end=" -> ")
        current = next_node[current]

    print("None")


# Linked list: 10 -> 20 -> 30 -> 40 -> None
next_node = {
    10: 20,
    20: 30,
    30: 40,
    40: None
}

head = 10

print("Before deletion:")
print_list(next_node, head)

head = delete_node(next_node, head, 30)

print("After deletion:")
print_list(next_node, head)
