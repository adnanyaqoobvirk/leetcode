"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited, q = {node: Node(node.val)}, [node]
        while q:
            nq = []
            for curr in q:
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val)
                        nq.append(neighbor)
                    visited[curr].neighbors.append(visited[neighbor])
            q = nq
        return visited[node]
                
                