"""Add two numbers whose digits are stored in linked lists."""


class Node:
    """One digit in a linked list."""

    def __init__(self, digit):
        self.digit = digit
        self.next = None


def create_linked_list(digits):
    """Create a linked list from digits, starting with the ones digit."""
    if len(digits) == 0:
        return None

    head = Node(digits[0])
    current_node = head

    for digit in digits[1:]:
        current_node.next = Node(digit)
        current_node = current_node.next

    return head


def print_linked_list(head):
    """Print the digits in the order they are stored."""
    current_node = head

    while current_node is not None:
        print(current_node.digit, end="")

        if current_node.next is not None:
            print(" -> ", end="")

        current_node = current_node.next

    print()


def add_two_numbers(first_number, second_number):
    """Return the sum as a new linked list.

    The ones digit is at the head of each input list.
    For example, 2 -> 4 -> 3 represents the number 342.
    """
    # The dummy node makes it easy to attach the first answer digit.
    answer_head = Node(0)
    answer_tail = answer_head
    carry = 0

    # Two empty lists represent zero plus zero.
    if first_number is None and second_number is None:
        return Node(0)

    while first_number is not None or second_number is not None or carry > 0:
        first_digit = 0
        second_digit = 0

        # If a list has run out of digits, treat its next digit as zero.
        if first_number is not None:
            first_digit = first_number.digit
            first_number = first_number.next

        if second_number is not None:
            second_digit = second_number.digit
            second_number = second_number.next

        # Add the two digits and any carry left over from the last step.
        digit_sum = first_digit + second_digit + carry
        answer_digit = digit_sum % 10
        carry = digit_sum // 10

        answer_tail.next = Node(answer_digit)
        answer_tail = answer_tail.next

    return answer_head.next


if __name__ == "__main__":
    # 2 -> 4 -> 3 means 342, and 5 -> 6 -> 4 means 465.
    first_number = create_linked_list([2, 4, 3])
    second_number = create_linked_list([5, 6, 4])

    print("First number digits:")
    print_linked_list(first_number)
    print("Second number digits:")
    print_linked_list(second_number)

    answer = add_two_numbers(first_number, second_number)
    print("Sum digits:")
    print_linked_list(answer)
