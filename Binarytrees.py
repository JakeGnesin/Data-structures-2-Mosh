class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def is_equal(self, other_tree):
        return self._is_equal_recursive(self.root, other_tree.root)

    def _is_equal_recursive(self, node1, node2):
        # Base cases: both nodes are None (subtrees are equal)
        if node1 is None and node2 is None:
            return True
        # One node is None, the other isn't (subtrees differ)
        if node1 is None or node2 is None:
            return False
        # Check if current nodes have same value and their subtrees are equal
        return (node1.value == node2.value and
                self._is_equal_recursive(node1.left, node2.left) and
                self._is_equal_recursive(node1.right, node2.right))

    def find_nodes_at_k_distance(self, k):
        result = []
        self._find_nodes_at_k_distance_helper(self.root, k, result)
        return result

    def _find_nodes_at_k_distance_helper(self, node, k, result):
        # Base cases
        if node is None:
            return

        # If k is 0, we've reached the desired distance
        if k == 0:
            result.append(node.value)
            return

        # Recursively traverse left and right subtrees with k-1
        self._find_nodes_at_k_distance_helper(node.left, k - 1, result)
        self._find_nodes_at_k_distance_helper(node.right, k - 1, result)


# new class for validation (could put these methods into above class?)


    class BinarySearchTree:
        # ... existing methods like __init__, insert, postorder_traversal ...

        def validate_tree(self):
            # Use float('-inf') and float('inf') as initial bounds
            return self._validate_recursive(self.root, float('-inf'), float('inf'))

        def _validate_recursive(self, node, min_value, max_value):
            # Base case: empty node is valid
            if node is None:
                return True

            # Check if current node's value is within the valid range
            if node.value <= min_value or node.value >= max_value:
                return False

            # Recursively validate left and right subtrees
            # Left subtree: values must be < node.value and > min_value
            # Right subtree: values must be > node.value and < max_value
            return (self._validate_recursive(node.left, min_value, node.value) and
                    self._validate_recursive(node.right, node.value, max_value))


# Test the equality check
bst1 = BinarySearchTree()
bst2 = BinarySearchTree()
values = [10, 5, 15, 6, 1, 8, 12, 18, 17]
for value in values:
    bst1.insert(value)
    bst2.insert(value)

# Print post-order traversal to verify structure
print("BST1 Post-order:", bst1.postorder_traversal())
print("BST2 Post-order:", bst2.postorder_traversal())
# Check if trees are equal
print("Are trees equal?", bst1.is_equal(bst2))

# Create a different tree for comparison
bst3 = BinarySearchTree()
different_values = [10, 5, 15]  # Different structure/values
for value in different_values:
    bst3.insert(value)
print("BST3 Post-order:", bst3.postorder_traversal())
print("Are BST1 and BST3 equal?", bst1.is_equal(bst3))


# check if 2 values are siblings of same parent node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def are_siblings(root, value1, value2):
    if not root or value1 == value2:
        return False

    # Helper function to check if two values are children of the same parent
    def check_siblings(node, val1, val2):
        if not node:
            return False

        # Check if current node is the parent of both values
        if node.left and node.right:
            if (node.left.value == val1 and node.right.value == val2) or \
               (node.left.value == val2 and node.right.value == val1):
                return True

        # Recursively check left and right subtrees
        return check_siblings(node.left, val1, val2) or check_siblings(node.right, val1, val2)

    # this line calls the check sibs method on the root node
    return check_siblings(root, value1, value2)
