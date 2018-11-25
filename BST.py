class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        node = self.root
        while node is not None:
            if node.value < new_val:
                node = node.right
            else:
                node = node.left
        node = new_val
        
    def search(self, find_val):
        node = self.root
        while node != None:
            if node.value == find_val:
                return True 
            if node.value < find_val:
                node = node.right
            else:
                node = node.left

        return False

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)