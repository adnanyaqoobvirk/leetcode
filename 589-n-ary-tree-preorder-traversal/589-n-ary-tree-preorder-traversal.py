"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if root:
            stack = [root]
            while stack:
                current = stack.pop()
                ans.append(current.val)
                stack.extend(reversed(current.children))
        return ans