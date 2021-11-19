"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        def helper(current: 'Node') -> int:
            nonlocal dia
            
            if not current:
                return 0
            
            first_max = second_max = 0
            for node in current.children:
                curr = helper(node)
                if curr > first_max:
                    second_max, first_max = first_max, curr
                elif curr > second_max:
                    second_max = curr

            dia = max(dia, first_max + second_max)

            return 1 + first_max
        
        dia = 0
        helper(root)
        return dia