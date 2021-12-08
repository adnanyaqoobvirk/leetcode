# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            left_sum = helper(curr.left)
            right_sum = helper(curr.right)
            
            nonlocal tilt_sum
            tilt_sum += abs(left_sum - right_sum)
            
            return curr.val + left_sum + right_sum
        
        tilt_sum = 0
        helper(root)
        return tilt_sum