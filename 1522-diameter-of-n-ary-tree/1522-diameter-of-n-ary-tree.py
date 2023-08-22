"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        def helper(curr: 'Node') -> int:
            if not curr:
                return 0
            
            first_max = second_max = 0
            for child in curr.children:
                h = helper(child)
                if first_max < h:
                    second_max, first_max = first_max, h
                elif second_max < h:
                    second_max = h
            
            self.d = max(self.d, first_max + second_max)
            
            return first_max + 1
        self.d = 0
        helper(root)
        return self.d