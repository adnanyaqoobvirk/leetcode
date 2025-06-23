"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue
            
            tail = curr.child
            while tail.next:
                tail = tail.next
            
            if curr.next:
                curr.next.prev = tail
            tail.next = curr.next
            
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

            curr = curr.next
        return head
        