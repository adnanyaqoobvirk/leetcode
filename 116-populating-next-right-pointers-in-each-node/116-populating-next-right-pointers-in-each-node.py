"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            q = [root]
            while q:
                nq, prev = [], None
                for node in q:
                    if prev:
                        prev.next = node

                    prev = node
                    if node.left:
                        nq.append(node.left)
                    if node.right:
                        nq.append(node.right)
                q = nq
        return root