"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        
        ans, q = [], [root]
        while q:
            nq, level = [], []
            for node in q:
                level.append(node.val)
                if node.children:
                    nq.extend(node.children)
            if level:
                ans.append(level)
            q = nq
        return ans