class LinkedBinaryTree:
    def __init__(self, root):
        self.root = root

    def insert_left(self, new_node):
        if self.root.left is None:
            self.root.left = new_node

    def insert_right(self, new_node):
        if self.root.right is None:
            self.root.right = new_node



