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
            return None
        
        node_map = {}
        
        prev, curr = None, head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        ncurr = sentinal = Node(0)
        curr = head
        while curr:
            ncurr.next = node_map[curr]
            if curr.random:
                ncurr.next.random = node_map[curr.random]
            ncurr, curr = ncurr.next, curr.next
        
        return sentinal.next