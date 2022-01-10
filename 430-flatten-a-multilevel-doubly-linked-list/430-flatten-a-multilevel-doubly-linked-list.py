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
        def helper(curr: Node) -> Node:
            prev = None
            while curr:
                if curr.child:
                    tail = helper(curr.child)
                    tail.next, curr.child.prev, curr.next, curr.child = curr.next, curr, curr.child, None
                    if tail.next: tail.next.prev = tail
                    prev, curr = tail, tail.next
                else:
                    prev, curr = curr, curr.next
            return prev
        helper(head)
        return head