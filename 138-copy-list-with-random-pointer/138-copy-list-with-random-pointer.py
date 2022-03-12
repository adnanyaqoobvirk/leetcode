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
        
        nodes = defaultdict(Node)
        ncurr = sentinal = Node(0)
        curr, nodes[head] = head, Node(head.val)
        while curr:
            node = nodes[curr]
            if curr.random:
                if curr.random not in nodes:
                    nodes[curr.random] = Node(curr.random.val)
                node.random = nodes[curr.random] = nodes[curr.random]
                
            if curr.next:
                if curr.next not in nodes:
                    nodes[curr.next] = Node(curr.next.val)
                node.next = nodes[curr.next] = nodes[curr.next]
            
            curr, ncurr.next, ncurr = curr.next, node, node
        return sentinal.next