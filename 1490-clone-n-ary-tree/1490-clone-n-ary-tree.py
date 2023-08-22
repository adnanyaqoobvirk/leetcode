"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        nroot = None
        q = [(root, None)]
        while q:
            nq = []
            for node, parent in q:
                nnode = Node(node.val, [])
                if not nroot:
                    nroot = nnode
                if parent:
                    parent.children.append(nnode)
                for child in node.children:
                    nq.append((child, nnode))
            q = nq
        return nroot