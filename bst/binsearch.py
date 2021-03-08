#!/usr/bin/env python3

"""
The difference between a binary tree and a BST is the entries are ordered in
a BST.

See ../bintree/binary_tree.py for explanation of what a binary tree is
"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already present in the tree.")

    def search(self, data):
        if self.root:
            is_found = self._search(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _search(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._search(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._search(data, current_node.left)
        if data == current_node.data:
            return True

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, current_node):
        if current_node:
            self._inorder_print_tree(current_node.left)
            print(str(current_node.data))
            self._inorder_print_tree(current_node.right)
            print(str(current_node.data))

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)

            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, current_node, data):
        if current_node.left:
            if data > current_node.left.data:
                return self._is_bst_satisfied(current_node.left, current_node.left.data)
            else:
                return False

        if current_node.right:
            if data < current_node.right.data:
                return self._is_bst_satisfied(current_node.right, current_node.right.data)
            else:
                return False


bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

print(bst.search(5))
print(bst.search(8))
print(bst.search(11))
print(bst.search(10))
print(bst.search(12))

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

print(bst.inorder_print_tree())

print(tree.inorder_print_tree())

print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())
