"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if root:
            stack = [[root, False]]
            while stack:
                current, processed = stack[-1]
                if not processed:
                    stack[-1][1] = True
                    if current.children:
                        for i in range(len(current.children) - 1, -1, -1):
                            stack.append([current.children[i], False])
                else:
                    ans.append(current.val)
                    stack.pop()
        return ans