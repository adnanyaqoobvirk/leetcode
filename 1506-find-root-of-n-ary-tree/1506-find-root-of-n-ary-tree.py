"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        hasParent = set()
        for node in tree:
            for child in node.children:
                hasParent.add(child)
        for node in tree:
            if node not in hasParent:
                return node