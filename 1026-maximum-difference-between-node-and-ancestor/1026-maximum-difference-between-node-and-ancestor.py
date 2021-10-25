# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(current: TreeNode, curr_max: int, curr_min: int):
            nonlocal max_diff
            
            if current:
                max_diff = max(abs(current.val - curr_min), abs(current.val - curr_max), max_diff)
                
                curr_min, curr_max = min(current.val, curr_min), max(current.val, curr_max)
                helper(current.left, curr_max, curr_min)
                helper(current.right, curr_max, curr_min)
        
        max_diff = 0
        helper(root, root.val, root.val)
        return max_diff