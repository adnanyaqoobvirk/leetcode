# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(current: TreeNode, curr_max: int, curr_min: int) -> int:
            if not current:
                return curr_max - curr_min
            
            curr_min, curr_max = min(current.val, curr_min), max(current.val, curr_max)
            return max(
                helper(current.left, curr_max, curr_min), 
                helper(current.right, curr_max, curr_min)
            )
        return helper(root, root.val, root.val)