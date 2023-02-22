# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(curr):
            lo, hi = curr.val, curr.val
            if curr.left:
                lo, left_hi, left_status = helper(curr.left)
                if not left_status or curr.val <= lo or curr.val <= left_hi:
                    return -inf, inf, False
            
            if curr.right:
                right_lo, hi, right_status = helper(curr.right)
                if not right_status or curr.val >= right_lo or curr.val >= hi:
                    return -inf, inf, False
            
            return lo, hi, True
        _, _, ans = helper(root)
        return ans