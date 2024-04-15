# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recurse(curr, total):
            if not curr:
                return 0
            
            total = total * 10 + curr.val
            
            if not curr.left and not curr.right:
                return total
            
            return recurse(curr.left, total) + recurse(curr.right, total)
        
        return recurse(root, 0)