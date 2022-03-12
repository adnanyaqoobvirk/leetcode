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
        def helper(curr: 'Optional[Node]') -> 'Optional[Node]':
            if curr:
                node_map[curr] = node = Node(curr.val)
                node.next = helper(curr.next)
                if curr.random:
                    node.random = node_map[curr.random]
                return node
        node_map = defaultdict(Node)
        return helper(head)