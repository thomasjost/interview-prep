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

    def delete(self):
        pass


bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.search(5))
print(bst.search(8))
print(bst.search(11))
print(bst.search(10))
print(bst.search(12))
