
# Implement Two Stacks Using One Array
#
# Stack 1 grows from LEFT to RIGHT.
# Stack 2 grows from RIGHT to LEFT.
#
# Both stacks share the same array.


class TwoStacks:

    def __init__(self, capacity):

        # Create one array for both stacks.
        self.capacity = capacity
        self.arr = [None] * capacity

        # Stack 1 starts before index 0.
        self.top1 = -1

        # Stack 2 starts after the last index.
        self.top2 = capacity

    def is_full(self):

        # Array is full when both stack tops meet
        # or become adjacent.
        return self.top1 + 1 == self.top2

    def is_stack1_empty(self):

        # Stack 1 is empty when top1 is -1.
        return self.top1 == -1

    def is_stack2_empty(self):

        # Stack 2 is empty when top2 reaches capacity.
        return self.top2 == self.capacity

    def push1(self, value):

        # Check if there is space in the shared array.
        if self.is_full():
            print("Stack Overflow! Array is full")
            return

        # Move Stack 1 top one position to the right.
        self.top1 += 1

        # Insert value at the new top position.
        self.arr[self.top1] = value

        print(value, "pushed into Stack 1")

    def push2(self, value):

        # Check if there is space in the shared array.
        if self.is_full():
            print("Stack Overflow! Array is full")
            return

        # Move Stack 2 top one position to the left.
        self.top2 -= 1

        # Insert value at the new top position.
        self.arr[self.top2] = value

        print(value, "pushed into Stack 2")

    def pop1(self):

        # Check whether Stack 1 is empty.
        if self.is_stack1_empty():
            print("Stack 1 Underflow!")
            return None

        # Get the top value of Stack 1.
        value = self.arr[self.top1]

        # Clear the old position.
        self.arr[self.top1] = None

        # Move Stack 1 top one position backward.
        self.top1 -= 1

        print(value, "popped from Stack 1")
        return value

    def pop2(self):

        # Check whether Stack 2 is empty.
        if self.is_stack2_empty():
            print("Stack 2 Underflow!")
            return None

        # Get the top value of Stack 2.
        value = self.arr[self.top2]

        # Clear the old position.
        self.arr[self.top2] = None

        # Move Stack 2 top one position backward.
        self.top2 += 1

        print(value, "popped from Stack 2")
        return value

    def display(self):

        # Show the complete shared array.
        print("Shared Array:", self.arr)

        # Display Stack 1 from bottom to top.
        print("Stack 1:", self.arr[:self.top1 + 1])

        # Display Stack 2 from bottom to top.
        print("Stack 2:", self.arr[self.top2:])


# Create two stacks with a shared capacity of 6.
stacks = TwoStacks(6)

# Insert values into Stack 1.
stacks.push1(10)
stacks.push1(20)

# Insert values into Stack 2.
stacks.push2(100)
stacks.push2(200)

# Display both stacks.
stacks.display()

# Remove one element from each stack.
stacks.pop1()
stacks.pop2()

# Display updated stacks.
stacks.display()
