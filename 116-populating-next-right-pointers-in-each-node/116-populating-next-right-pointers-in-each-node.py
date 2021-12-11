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
        def helper(curr: Optional[Node], nxt: Optional[Node]) -> None:
            if curr:
                curr.next = nxt
                helper(curr.left, curr.right)
                helper(curr.right, nxt.left if nxt else None)
        helper(root, None)
        return root
            