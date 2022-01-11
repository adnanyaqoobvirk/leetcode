"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
    
        prev, curr = head, head.next
        while curr != head:
            if prev.val <= insertVal <= curr.val:
                break
            elif prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                break
            prev, curr = curr, curr.next
        prev.next = Node(insertVal, prev.next)
        return head