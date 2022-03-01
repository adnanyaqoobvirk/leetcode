"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def __init__(self) -> None:
        self.seen = {}
        
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None

        if root not in self.seen:
            self.seen[root] = nroot = Node(root.val)
            for child in root.children:
                nroot.children.append(self.cloneTree(child))
            
        return self.seen[root]