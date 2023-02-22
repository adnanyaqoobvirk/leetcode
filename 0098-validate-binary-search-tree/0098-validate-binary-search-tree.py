# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(curr):
            nonlocal prev
            if not curr:
                return True
            
            if not helper(curr.left) or prev >= curr.val:
                return False
            prev = curr.val
            if not helper(curr.right):
                return False
            
            return True
        prev = -inf
        return helper(root)