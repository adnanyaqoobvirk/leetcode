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
        def dfs(curr: Optional['Node']) -> Optional['Node']:
            if not curr:
                return None

            new_curr = Node(curr.val)
            node_map[curr] = new_curr
            
            for nei in curr.neighbors:
                if nei not in node_map:
                    new_nei = dfs(nei)
                    node_map[nei] = new_nei
                
                new_curr.neighbors.append(node_map[nei])
            
            return new_curr
        
        node_map = {}
        return dfs(node)