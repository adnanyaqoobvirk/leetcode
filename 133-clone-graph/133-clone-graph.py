"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self) -> None:
        self.seen = {}
        
    def cloneGraph(self, root: 'Node') -> 'Node':
        if not root: return None

        if root not in self.seen:
            nroot = self.seen[root] = Node(root.val)
            for child in root.neighbors:
                nroot.neighbors.append(self.cloneGraph(child))
        return self.seen[root]