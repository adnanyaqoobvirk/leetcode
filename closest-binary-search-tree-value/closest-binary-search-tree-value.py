# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff, ans = float('inf'), None
        while root:
            root_diff = root.val - target
            if abs(root_diff) < min_diff:
                min_diff, ans = abs(root_diff), root.val
                
            if root_diff < 0:
                root = root.right
            else:
                root = root.left
        return ans