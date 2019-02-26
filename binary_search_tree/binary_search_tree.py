class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        inserted = False
        cur_node = self
        while not inserted:
            # If there are no nodes in the tree, create the root from the value.
            if not self.value:
                self.value = value
                inserted = True
            # Otherwise, iterate through the existing nodes until you come to a
            # leaf, then insert new node with value.
            elif value < cur_node.value and cur_node.left == None:
                cur_node.left = Node(value)
                inserted = True
            elif value > cur_node.value and cur_node.right == None:
                cur_node.right = Node(value)
                inserted = True
            elif value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
            else:
                print("Value already in tree")

    def contains(self, target):
        cur_node = self
        while True:
            # If there is no root, return False.
            if not self.value:
                return False
            # If cur_node is None, we've hit a leaf, and the target isn't in
            # the tree. Return False.
            if not cur_node:
                return False
            # Otherwise, iterate through the tree until the target is found and
            # return True, or a leaf is hit and return False.
            if target == cur_node.value:
                return True
            elif target < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

    def get_max(self):
        cur_node = self
        # Just walk the right side of the tree until we hit a leaf, resulting
        # in the max value.
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node.value
