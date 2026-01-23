"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr = stack.pop()
            for nei in curr.neighbors:
                if nei not in node_map:
                    node_map[nei] = Node(nei.val)
                    stack.append(nei)
                node_map[curr].neighbors.append(node_map[nei])
        return node_map[node]