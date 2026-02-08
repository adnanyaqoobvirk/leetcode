# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            left = helper(curr.left)
            right = helper(curr.right)
            
            if abs(right - left) > 1:
                return inf
            else:
                return max(left, right) + 1
            
        ans = helper(root)
        return True if ans != inf else False