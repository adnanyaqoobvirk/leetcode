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
        def _flatten(curr: 'Optional[Node]') -> 'Optional[Node]':
            if not curr:
                return
            
            if curr.child:
                nxt = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                tail = _flatten(curr.child)
                curr.child = None
                tail.next = nxt
                if nxt:
                    nxt.prev = tail

            if not curr.next:
                return curr

            return _flatten(curr.next)

        _flatten(head)

        return head
        