"""
File: btnode.py
Author: Ken Lambert
"""

class Node(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, board, left = None, right = None):
        self.board = board
        self.left = left
        self.right = right
