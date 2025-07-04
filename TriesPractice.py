class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Array for a-z (26 lowercase letters)
        self.is_end_of_word = False  # Flag to mark end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize root node

    def insert_word(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word: The word to insert.

        Raises:
            TypeError: If word is not a string.
            ValueError: If word is empty or contains non-lowercase letters.
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            raise ValueError("Word cannot be empty")
        for char in word:
            if not ('a' <= char <= 'z'):
                raise ValueError(
                    "Word must contain only lowercase letters a-z")

        curr = self.root
        for char in word:
            index = ord(char) - ord('a')  # Map 'a' to 0, 'b' to 1, etc.
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end_of_word = True

    def contains_word(self, word: str) -> bool:
        """
        Check if a word exists in the Trie and is marked as complete.

        Args:
            word: The word to check.

        Returns:
            bool: True if the word is complete, False otherwise.

        Raises:
            TypeError: If word is not a string.
            ValueError: If word is empty or contains non-lowercase letters.
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            raise ValueError("Word cannot be empty")
        for char in word:
            if not ('a' <= char <= 'z'):
                raise ValueError(
                    "Word must contain only lowercase letters a-z")

        curr = self.root
        for char in word:
            index = ord(char) - ord('a')  # Map 'a' to 0, 'b' to 1, etc.
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.is_end_of_word

    def remove_word(self, word: str) -> None:
        """
        Remove a word from the Trie using recursion.

        Args:
            word: The word to remove.

        Raises:
            TypeError: If word is not a string.
            ValueError: If word is empty or contains non-lowercase letters.
        """
        def _remove_recursive(node: TrieNode, word: str, index: int) -> bool:
            """
            Helper method to recursively remove a word.

            Args:
                node: Current node in the Trie.
                word: The word being removed.
                index: Current character index in the word.

            Returns:
                bool: True if the current node can be deleted, False otherwise.
            """
            # Base case: reached the end of the word
            if index == len(word):
                if not node.is_end_of_word:
                    return False  # Word not found
                node.is_end_of_word = False  # Unmark as end of word
                # Return True if node has no children and is not end of another word
                return not any(node.children)

            char = word[index]
            char_index = ord(char) - ord('a')
            if not node.children[char_index]:
                return False  # Word not found

            # Recursively remove the next character
            should_delete_child = _remove_recursive(
                node.children[char_index], word, index + 1)

            # If child can be deleted, remove it
            if should_delete_child:
                node.children[char_index] = None
                # Return True if current node has no children and is not end of a word
                return not any(node.children) and not node.is_end_of_word

            # Node cannot be deleted (has other children or is end of a word)
            return False

        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            raise ValueError("Word cannot be empty")
        for char in word:
            if not ('a' <= char <= 'z'):
                raise ValueError(
                    "Word must contain only lowercase letters a-z")

        _remove_recursive(self.root, word, 0)

    def autocomplete(self, prefix: str) -> list[str]:
        """
        Return a list of words in the Trie that start with the given prefix.

        Args:
            prefix: The prefix to search for.

        Returns:
            list[str]: List of complete words starting with the prefix.

        Raises:
            TypeError: If prefix is not a string.
            ValueError: If prefix contains non-lowercase letters.
        """
        def _collect_words(node: TrieNode, current_word: str, words: list) -> None:
            """
            Helper method to recursively collect all words from a given node.

            Args:
                node: Current node in the Trie.
                current_word: The word built so far.
                words: List to store collected words.
            """
            if node.is_end_of_word:
                words.append(current_word)

            for i in range(26):
                if node.children[i]:
                    char = chr(i + ord('a'))
                    _collect_words(
                        node.children[i], current_word + char, words)

        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        for char in prefix:
            if not ('a' <= char <= 'z'):
                raise ValueError(
                    "Prefix must contain only lowercase letters a-z")

        # Traverse to the node corresponding to the prefix
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return []  # Prefix not found
            curr = curr.children[index]

        # Collect all words starting from the prefix's node
        words = []
        _collect_words(curr, prefix, words)
        return words

    def count_words(self) -> int:
        """
        Count the total number of complete words in the Trie.

        Returns:
            int: Number of words in the Trie.
        """
        def _count_recursive(node: TrieNode) -> int:
            """
            Helper method to recursively count words.

            Args:
                node: Current node in the Trie.

            Returns:
                int: Number of complete words in the subtree rooted at node.
            """
            count = 1 if node.is_end_of_word else 0
            for i in range(26):
                if node.children[i]:
                    count += _count_recursive(node.children[i])
            return count

        return _count_recursive(self.root)

    def print_trie(self, node=None, prefix="", level=0):
        if node is None:
            node = self.root
        print("  " * level + prefix + ("$" if node.is_end_of_word else ""))
        for i in range(26):
            if node.children[i]:
                char = chr(i + ord('a'))
                self.print_trie(node.children[i], char, level + 1)


def test_trie():
    trie = Trie()
    words_to_insert = ["cat", "car", "cart", "bat", "cats"]
    for word in words_to_insert:
        trie.insert_word(word)
        print(f"Inserted: {word}")

    print("\nTrie structure before removal:")
    trie.print_trie()

    # Test contains_word before removal
    test_cases = ["cat", "car", "cart", "bat", "ca", "cats"]
    for word in test_cases:
        result = trie.contains_word(word)
        print(f"Contains '{word}'? {result}")

    # Test autocomplete
    print("\nAutocomplete tests:")
    prefixes = ["ca", "b", "d", ""]
    for prefix in prefixes:
        result = trie.autocomplete(prefix)
        print(f"Words starting with '{prefix}': {result}")

    # Test removal
    remove_words = ["cat", "cart", "dog"]
    for word in remove_words:
        print(f"\nRemoving '{word}':")
        trie.remove_word(word)
        print("Trie structure after removal:")
        trie.print_trie()
        # Check if removed word is gone and others remain
        for test_word in test_cases:
            result = trie.contains_word(test_word)
            print(f"Contains '{test_word}' after removing '{word}'? {result}")

    # Test error handling
    print("\nError handling tests:")
    try:
        trie.contains_word(123)
    except TypeError as e:
        print(f"Error: {e}")
    try:
        trie.contains_word("")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        trie.contains_word("Cat")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        trie.remove_word(123)
    except TypeError as e:
        print(f"Error: {e}")
    try:
        trie.remove_word("")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        trie.remove_word("Cat")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_trie()


# using a dictionary instead of array
class TrieNode:
    """Represents a node in the Trie, storing child nodes in a dictionary."""

    def __init__(self):
        self._children = {}  # Dictionary to store child nodes (char: TrieNode)
        self._is_end_of_word = False  # Flag to mark end of a word

    @property
    def children(self):
        """Getter for children dictionary."""
        return self._children

    @property
    def is_end_of_word(self):
        """Getter for is_end_of_word flag."""
        return self._is_end_of_word

    @is_end_of_word.setter
    def is_end_of_word(self, value):
        """Setter for is_end_of_word flag."""
        self._is_end_of_word = value


class Trie:
    """A Trie data structure for storing and querying words."""

    def __init__(self):
        """Initialize the Trie with an empty root node."""
        self._root = TrieNode()

    def insert_word(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word: The word to insert.
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            return  # Ignore empty strings

        curr = self._root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def is_end_of_word(self, word: str) -> bool:
        """
        Check if a word exists in the Trie and is marked as complete.

        Args:
            word: The word to check.

        Returns:
            bool: True if the word is complete, False otherwise.
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            return False

        curr = self._root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def print_trie(self, node: TrieNode = None, prefix: str = "", level: int = 0) -> None:
        """
        Print a text-based visualization of the Trie structure.

        Args:
            node: The current node (defaults to root).
            prefix: The character at the current node.
            level: The depth for indentation.
        """
        if node is None:
            node = self._root
        print("  " * level + prefix + ("$" if node.is_end_of_word else ""))
        # Sort children for consistent output
        for char in sorted(node.children.keys()):
            self.print_trie(node.children[char], char, level + 1)


def test_trie():
    """Test the Trie functionality and visualize its structure."""
    trie = Trie()
    # Insert test words, including "cats"
    words_to_insert = ["cat", "car", "cart", "bat", "cats"]
    for word in words_to_insert:
        trie.insert_word(word)
        print(f"Inserted: {word}")

    # Test is_end_of_word
    test_cases = ["cat", "car", "cart", "bat", "ca", "cats"]
    for word in test_cases:
        result = trie.is_end_of_word(word)
        print(f"Is '{word}' a complete word? {result}")

    # Visualize the Trie
    print("\nTrie structure:")
    trie.print_trie()

    # Test error handling
    try:
        trie.insert_word(123)  # Should raise TypeError
    except TypeError as e:
        print(f"\nError handling test: {e}")


if __name__ == "__main__":
    test_trie()
