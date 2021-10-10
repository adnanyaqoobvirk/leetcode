"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        def recurse(current: int) -> int:
            if not current:
                return 0
            
            mx = smx = 0
            for child in current.children:
                height = recurse(child)
                if height > mx:
                    smx, mx = mx, height
                elif height > smx:
                    smx = height
                    
            height = 1 + mx
            diameter[0] = max(diameter[0], height + smx)
            return height
                
        diameter = [0]
        recurse(root)
        return diameter[0] - 1