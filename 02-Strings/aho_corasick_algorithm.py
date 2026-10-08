"""Find many patterns in a string using the Aho-Corasick algorithm."""

from collections import deque


class TrieNode:
    """A node in the pattern trie used by Aho-Corasick."""

    def __init__(self):
        self.children = {}
        self.failure_link = None
        self.output = []


class AhoCorasick:
    """Search for several patterns in one pass through a text."""

    def __init__(self, patterns):
        self.root = TrieNode()
        self.root.failure_link = self.root

        self._build_trie(patterns)
        self._build_failure_links()

    def _build_trie(self, patterns):
        """Store every non-empty pattern in a trie."""
        for pattern in patterns:
            if pattern == "":
                # Empty patterns are ignored to avoid zero-length matches.
                continue

            current_node = self.root

            for character in pattern:
                if character not in current_node.children:
                    current_node.children[character] = TrieNode()

                current_node = current_node.children[character]

            current_node.output.append(pattern)

    def _build_failure_links(self):
        """Connect trie nodes to the next possible matching prefix."""
        nodes_to_visit = deque()

        # Every first-level node falls back to the root.
        for child_node in self.root.children.values():
            child_node.failure_link = self.root
            nodes_to_visit.append(child_node)

        while nodes_to_visit:
            current_node = nodes_to_visit.popleft()

            for character, child_node in current_node.children.items():
                fallback_node = current_node.failure_link

                while (
                    fallback_node is not self.root
                    and character not in fallback_node.children
                ):
                    fallback_node = fallback_node.failure_link

                if character in fallback_node.children:
                    child_node.failure_link = fallback_node.children[character]
                else:
                    child_node.failure_link = self.root

                # Patterns ending at the fallback node also end here.
                child_node.output.extend(child_node.failure_link.output)
                nodes_to_visit.append(child_node)

    def search(self, text):
        """Return (pattern, start_index) pairs for every match in text."""
        matches = []
        current_node = self.root
        text_index = 0

        while text_index < len(text):
            character = text[text_index]

            while (
                current_node is not self.root
                and character not in current_node.children
            ):
                current_node = current_node.failure_link

            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                current_node = self.root

            for pattern in current_node.output:
                start_index = text_index - len(pattern) + 1
                matches.append((pattern, start_index))

            text_index += 1

        return matches


patterns = ["he", "she", "his", "hers"]
text = "ushers"
searcher = AhoCorasick(patterns)
matches = searcher.search(text)

print(f"Patterns found in {text!r}:")
for pattern, start_index in matches:
    print(f"{pattern!r} starts at index {start_index}")

overlapping_searcher = AhoCorasick(["a", "aa"])
print(f"Overlapping matches: {overlapping_searcher.search('aaa')}")
