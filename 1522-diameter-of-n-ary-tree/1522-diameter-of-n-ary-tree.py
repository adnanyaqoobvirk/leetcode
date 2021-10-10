"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def dfs(self, current: int) -> int:
        if not current:
            return 0

        first = second = 0
        for child in current.children:
            height = self.dfs(child)
            if height > first:
                second, first = first, height
            elif height > second:
                second = height
                
        self.dia = max(self.dia, first + second)
        return 1 + first
    
    def diameter(self, root: 'Node') -> int:
        self.dia = 0
        self.dfs(root)
        return self.dia