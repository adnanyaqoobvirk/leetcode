# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(curr, num):
            if not curr:
                return 0
            
            if not curr.left and not curr.right:
                return 10 * num + curr.val
            
            return helper(curr.left, num * 10 + curr.val) + helper(curr.right, num * 10 + curr.val)
        return helper(root, 0)