# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        current = root
        closest = diff = float('inf')
        while current:
            curr_diff = abs(current.val - target)
            if curr_diff < diff:
                closest, diff = current.val, curr_diff
                
            current = current.left if current.val > target else current.right
        return closest