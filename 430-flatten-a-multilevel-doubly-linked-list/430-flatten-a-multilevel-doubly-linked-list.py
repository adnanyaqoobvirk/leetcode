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
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        current = sentinal = Node(0, None, None, None)
        stack = [head]
        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                
            node.prev, node.child, current.next = current, None, node
            current = current.next
        sentinal.next.prev = None
        return sentinal.next