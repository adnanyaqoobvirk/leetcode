# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(curr):
            if not curr:
                return -inf
            
            left = helper(curr.left)
            right = helper(curr.right)
            
            curr_max = max(curr.val, curr.val + left, curr.val + right)
            
            nonlocal max_sum
            max_sum = max(
                max_sum, curr_max, curr.val + left + right
            )
            
            return curr_max
            
        max_sum = -inf
        helper(root)
        return max_sum