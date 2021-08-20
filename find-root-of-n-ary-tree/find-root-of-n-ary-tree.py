"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        childs = {child for node in tree for child in node.children}
        for node in tree:
            if node not in childs:
                return node
        return None
        