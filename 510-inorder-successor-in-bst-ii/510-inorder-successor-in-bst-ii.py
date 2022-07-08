"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        root = node
        while root.parent:
            root = root.parent
        
        node_found = False
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                
                if node_found:
                    return curr
                
                if curr == node:
                    node_found = True
                
                root = curr.right
        return None