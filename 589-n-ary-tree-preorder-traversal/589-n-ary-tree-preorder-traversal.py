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
                if current.children:
                    for i in range(len(current.children) - 1, -1, -1):
                        stack.append(current.children[i])
        return ans