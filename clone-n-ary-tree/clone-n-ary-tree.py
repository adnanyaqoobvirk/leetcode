"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        sentinal = Node()
        stack = [(root, sentinal)]
        while stack:
            current, parent = stack.pop()
            if current:
                parent.children.append(Node(current.val))
                for child in reversed(current.children):
                    stack.append((child, parent.children[-1]))
        return sentinal.children[-1] if sentinal.children else None