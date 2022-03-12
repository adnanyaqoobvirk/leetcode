"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next, curr.random)
            curr = curr.next.next
        
        curr = head
        while curr:
            if curr.next.random:
                curr.next.random = curr.next.random.next
            curr = curr.next.next
        
        curr, nhead = head, head.next
        while curr:
            ncurr = curr.next
            curr.next = curr.next.next
            if ncurr.next:
                ncurr.next = ncurr.next.next
            curr = curr.next
            
        return nhead