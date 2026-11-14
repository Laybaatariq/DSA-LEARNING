
# Implement LRU Cache using:
# 1. Hash Map
# 2. Doubly Linked List
#
# Most Recently Used -> Near Head
# Least Recently Used -> Near Tail
#
# Both get() and put() work in O(1) time.


# Doubly Linked List Node
class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value

        # Pointer to previous node.
        self.prev = None

        # Pointer to next node.
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        # Maximum number of items allowed.
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity

        # Dictionary provides O(1) average lookup.
        self.cache = {}

        # Dummy head and tail simplify insertion/deletion.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Initially, head and tail are connected.
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):

        # Get the nodes before and after current node.
        previous_node = node.prev
        next_node = node.next

        # Connect previous node directly to next node.
        previous_node.next = next_node
        next_node.prev = previous_node

    def add_to_front(self, node):

        # Insert node immediately after dummy head.
        # This position represents Most Recently Used.
        first_node = self.head.next

        node.prev = self.head
        node.next = first_node

        first_node.prev = node
        self.head.next = node

    def move_to_front(self, node):

        # Remove node from its current position.
        self.remove_node(node)

        # Reinsert it at the front.
        self.add_to_front(node)

    def get(self, key):

        # Check whether key exists in the cache.
        if key not in self.cache:
            return -1

        # Retrieve the corresponding node.
        node = self.cache[key]

        # Accessing a node makes it most recently used.
        self.move_to_front(node)

        return node.value

    def put(self, key, value):

        # If key already exists, update its value.
        if key in self.cache:

            node = self.cache[key]
            node.value = value

            # Updated item becomes most recently used.
            self.move_to_front(node)

            return

        # Create a new node.
        new_node = Node(key, value)

        # Store the node in the hash map.
        self.cache[key] = new_node

        # Add the new node at the front.
        self.add_to_front(new_node)

        # If capacity is exceeded, remove LRU item.
        if len(self.cache) > self.capacity:

            # Node before dummy tail is least recently used.
            lru_node = self.tail.prev

            # Remove it from the linked list.
            self.remove_node(lru_node)

            # Remove its key from the hash map.
            del self.cache[lru_node.key]

    def display(self):

        # Traverse from most recently used to least used.
        current = self.head.next

        print("Cache (MRU -> LRU):", end=" ")

        while current != self.tail:

            print(
                f"({current.key}: {current.value})",
                end=" -> "
            )

            current = current.next

        print("None")


# Create an LRU Cache with capacity 3.
lru = LRUCache(3)

# Insert three key-value pairs.
lru.put(1, 100)
lru.put(2, 200)
lru.put(3, 300)

lru.display()

# Access key 1.
# Key 1 becomes the most recently used item.
print("Get key 1:", lru.get(1))

lru.display()

# Insert key 4.
# Cache is full, so least recently used key 2 is removed.
lru.put(4, 400)

lru.display()

# Check removed and existing keys.
print("Get key 2:", lru.get(2))
print("Get key 3:", lru.get(3))

lru.display()

