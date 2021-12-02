"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self) -> None:
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            ans = Node(node.val, [])
            self.visited[node.val] = ans
            for v in node.neighbors:
                ans.neighbors.append(
                    self.cloneGraph(v) 
                    if v.val not in self.visited 
                    else self.visited[v.val]
                )
            return ans