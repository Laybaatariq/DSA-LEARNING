
# Check Balanced Parentheses Using Stack
#
# Examples:
# "{[()]}"  -> Balanced
# "{[(])}"  -> Not Balanced
# "((()))"  -> Balanced
# "({[]})"  -> Balanced


def is_balanced(expression):

    # Stack stores opening brackets.
    stack = []

    # Dictionary maps each closing bracket
    # to its corresponding opening bracket.
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Traverse every character in the expression.
    for char in expression:

        # If character is an opening bracket,
        # push it onto the stack.
        if char in "({[":
            stack.append(char)

        # If character is a closing bracket,
        # check whether it matches the stack top.
        elif char in ")}]":

            # If stack is empty, there is no
            # opening bracket available to match.
            if not stack:
                return False

            # Remove the most recent opening bracket.
            top = stack.pop()

            # Compare it with the expected opening bracket.
            if top != matching_brackets[char]:
                return False

    # Expression is balanced only if no
    # unmatched opening brackets remain.
    return len(stack) == 0


# Test cases
expressions = [
    "{[()]}",
    "{[(])}",
    "((()))",
    "({[]})",
    "(()",
    "())"
]

for expression in expressions:

    if is_balanced(expression):
        print(expression, "-> Balanced")
    else:
        print(expression, "-> Not Balanced")

