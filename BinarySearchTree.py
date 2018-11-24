class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        self.preorder_print(self.root)

    def preorder_search(self, node, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if node is None:
            return
        if node.value == find_val:
            print True 
        self.preorder_search(node.left, find_val)
        self.preorder_search(node.right, find_val)

    def preorder_print(self, node):
        """Helper method - use this to create a 
        recursive print solution."""
        if node is None:
            return
        print(node.value)
        self.preorder_print(node.left)
        self.preorder_print(node.right)
        


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
tree.search(4)
# Should be False
tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
tree.print_tree()