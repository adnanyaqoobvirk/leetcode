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
        else:
            prev, curr = head, head.next
            while prev.val <= curr.val and curr != head:
                prev, curr = curr, curr.next
            
            nhead = curr
            while curr.val < insertVal:
                prev, curr = curr, curr.next

                if curr == nhead:
                    break
            prev.next = Node(insertVal, curr)
        return head