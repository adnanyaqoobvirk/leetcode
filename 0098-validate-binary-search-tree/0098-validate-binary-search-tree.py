# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -inf, inf)]
        while stack:
            curr, lo, hi = stack.pop()
            if not curr:
                continue
            
            if curr.val <= lo or curr.val >= hi:
                return False
            
            stack.append((curr.left, lo, curr.val))
            stack.append((curr.right, curr.val, hi))
        return True