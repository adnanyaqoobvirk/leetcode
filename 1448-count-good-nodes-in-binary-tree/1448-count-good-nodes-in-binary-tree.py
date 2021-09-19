# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        ans = 0
        while stack:
            current, maximum = stack.pop()
            
            maximum = max(current.val, maximum)
            if current.val == maximum:
                ans += 1
            
            if current.right:
                stack.append((current.right, maximum))
            if current.left:
                stack.append((current.left, maximum))
        return ans