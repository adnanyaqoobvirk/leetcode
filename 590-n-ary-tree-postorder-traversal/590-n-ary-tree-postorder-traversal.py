"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def recurse(current: Node) -> None:
            if current:
                for child in current.children:
                    recurse(child)
                ans.append(current.val)
        
        ans = []
        recurse(root)
        return ans