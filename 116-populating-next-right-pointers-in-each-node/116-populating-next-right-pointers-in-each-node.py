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
        head = root
        while head and head.left:
            prev, curr = None, head
            while curr:
                if prev:
                    prev.right.next = curr.left
                curr.left.next = curr.right
                prev, curr = curr, curr.next
            head = head.left
        return root
                