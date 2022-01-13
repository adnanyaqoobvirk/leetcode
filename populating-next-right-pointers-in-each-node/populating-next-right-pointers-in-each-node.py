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
        lvl_head = root
        while lvl_head:
            lvl_head, prev, curr = lvl_head.left, None, lvl_head
            while curr and curr.left:
                if prev: prev.right.next = curr.left
                curr.left.next, prev, curr = curr.right, curr, curr.next
        return root