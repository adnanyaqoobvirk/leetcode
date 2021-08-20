"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        root = 0
        for node in tree:
            root ^= node.val
            for child in node.children:
                root ^= child.val
        
        for node in tree:
            if node.val == root:
                return node
        return None
        