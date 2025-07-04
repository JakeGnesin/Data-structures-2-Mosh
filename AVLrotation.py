class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.steps = []

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        if node:
            node.height = max(self._height(node.left),
                              self._height(node.right)) + 1

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def _handle_imbalance(self, root, key):
        balance = self._balance_factor(root)
        self.steps.append(
            f"Inserted {key}, Balance factor at {root.key}: {balance}")

        # Left-Left (LL)
        if balance > 1 and key < root.left.key:
            self.steps.append(f"LL imbalance at {root.key}, right rotation")
            return self._right_rotate(root)

        # Right-Right (RR)
        if balance < -1 and key > root.right.key:
            self.steps.append(f"RR imbalance at {root.key}, left rotation")
            return self._left_rotate(root)

        # Left-Right (LR)
        if balance > 1 and key > root.left.key:
            self.steps.append(
                f"LR imbalance at {root.key}, left-right rotation")
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right-Left (RL)
        if balance < -1 and key < root.right.key:
            self.steps.append(
                f"RL imbalance at {root.key}, right-left rotation")
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def insert(self, root, key):
        # Standard BST insert
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # No duplicates

        # Update height and handle imbalances
        self._update_height(root)
        return self._handle_imbalance(root, key)

    def is_balanced(self, root):
        if not root:
            return True

        # Check balance factor of current node
        balance = self._balance_factor(root)
        if balance < -1 or balance > 1:
            return False

        # Recursively check left and right subtrees
        return self.is_balanced(root.left) and self.is_balanced(root.right)

    def level_order(self, root):
        if not root:
            return "Empty"
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(str(node.key))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return " -> ".join(result)


def process_set(numbers, set_name):
    print(f"\n=== {set_name} ===")
    avl = AVLTree()
    root = None
    for key in numbers:
        print(f"\nInserting {key}:")
        avl.steps = []  # Reset steps for each insertion
        root = avl.insert(root, key)
        for step in avl.steps:
            print(step)
        print(f"Tree: {avl.level_order(root)}")
        print(f"Is balanced: {avl.is_balanced(root)}")


# Test sets
sets = [
    ([1, 2, 3, 4, 5], "Set 1"),
    ([5, 10, 3, 12, 15, 14], "Set 2"),
    ([12, 3, 9, 4, 6, 2], "Set 3")
]

# Run for each set
for numbers, set_name in sets:
    process_set(numbers, set_name)
