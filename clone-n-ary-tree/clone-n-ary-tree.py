"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root:
            copy = Node(root.val)
            for child in root.children:
                copy.children.append(self.cloneTree(child))
            return copy