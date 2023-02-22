# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(curr, lo = -inf, hi = inf):
            if not curr:
                return True
            
            if lo >= curr.val or curr.val >= hi:
                return False
            
            return helper(curr.left, lo, curr.val) and helper(curr.right, curr.val, hi)
        return helper(root)