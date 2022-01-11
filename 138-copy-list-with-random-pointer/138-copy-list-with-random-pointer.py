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
        if not head: return head
        
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        nhead, curr = head.next, head
        while curr:
            if curr.next.next:
                curr.next.next, curr.next, curr = curr.next.next.next, curr.next.next, curr.next.next
            else:
                curr.next, curr = curr.next.next, curr.next.next
                
        return nhead