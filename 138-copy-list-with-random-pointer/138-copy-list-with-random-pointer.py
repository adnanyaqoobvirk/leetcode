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
        
        randoms, sentinal = {}, Node(0)
        ocurr, curr = head, sentinal
        while ocurr:
            if ocurr not in randoms:
                randoms[ocurr] = Node(ocurr.val)
            curr.next = randoms[ocurr]
            
            if ocurr.random:
                if ocurr.random not in randoms:
                    randoms[ocurr.random] = Node(ocurr.random.val)
                curr.next.random = randoms[ocurr.random]
                
            if ocurr.next:
                if ocurr.next not in randoms:
                    randoms[ocurr.next] = Node(ocurr.next.val)
                curr.next.next = randoms[ocurr.next]
            ocurr, curr = ocurr.next, curr.next
        return sentinal.next