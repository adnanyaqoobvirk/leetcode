"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        @functools.cache
        def nodeCount(current: Node) -> int:
            if current:
                count = 1
                for child in current.children:
                    count += nodeCount(child)
                return count
            return 0
    
        n = len(tree)
        for node in tree:
            if nodeCount(node) == n:
                return node
        return None
        