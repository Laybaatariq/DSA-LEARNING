
def detect_loop(next_node, head):
    slow = head
    fast = head

    while fast is not None and next_node[fast] is not None:
        slow = next_node[slow]
        fast = next_node[next_node[fast]]

        if slow == fast:
            return True

    return False


# Each node points to the next node
next_node = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 3
}

head = 1

if detect_loop(next_node, head):
    print("Loop detected!")
else:
    print("No loop detected!")
