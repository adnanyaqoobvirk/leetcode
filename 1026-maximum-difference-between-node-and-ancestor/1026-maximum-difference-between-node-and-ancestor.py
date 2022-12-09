# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(curr):
            if not curr:
                return inf, -inf
            
            min_left, max_left = helper(curr.left)
            min_right, max_right = helper(curr.right)
            
            mn, mx = min(min_left, min_right), max(max_left, max_right)
            
            nonlocal max_diff
            if mn != inf:
                max_diff = max(max_diff, abs(curr.val - mn))
            
            if mx != -inf:
                max_diff = max(max_diff, abs(mx - curr.val))
            
            return min(mn, curr.val), max(mx, curr.val)
        
        max_diff = -inf
        helper(root)
        return max_diff