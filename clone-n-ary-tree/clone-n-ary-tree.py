"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def clone(current: 'Node', parent: 'Node') -> None:
            if current:
                parent.children.append(Node(current.val))
                for child in current.children:
                    clone(child, parent.children[-1])
        
        sentinal = Node()
        clone(root, sentinal)
        return sentinal.children[-1] if sentinal.children else None