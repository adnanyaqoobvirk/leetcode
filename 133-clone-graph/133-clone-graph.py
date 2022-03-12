"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.processed = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            if node in self.processed:
                return self.processed[node]
            
            self.processed[node] = curr = Node(node.val)
            for neighbor in node.neighbors:
                n = self.cloneGraph(neighbor)
                if n:
                    curr.neighbors.append(n)
            return curr