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
        
        SUB_GRAPH_DONE = True
        SUB_GRAPH_NOT_DONE = False

        node_map = {node: Node(node.val)}
        stack = [(node, SUB_GRAPH_NOT_DONE)]
        while stack:
            curr, is_sub_graph_done = stack.pop()

            if is_sub_graph_done:
                new_curr = node_map[curr]
                for nei in curr.neighbors:
                    new_curr.neighbors.append(node_map[nei])
            else:
                stack.append((curr, SUB_GRAPH_DONE))
                for nei in curr.neighbors:
                    if nei in node_map:
                        continue
                    node_map[nei] = Node(nei.val)
                    stack.append((nei, SUB_GRAPH_NOT_DONE))
        
        return node_map[node]