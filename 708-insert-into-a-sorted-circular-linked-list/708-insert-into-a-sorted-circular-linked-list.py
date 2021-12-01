"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        sentinal = Node(None, head)
        prev, curr = sentinal, head
        while curr and prev != curr:
            if prev.val:
                if prev.val <= insertVal <= curr.val or (curr.val < prev.val and (insertVal <= curr.val or insertVal >= prev.val)):
                    break
            prev, curr = curr, curr.next
            if curr == head:
                break
        prev.next = Node(insertVal, curr)
        return sentinal.next