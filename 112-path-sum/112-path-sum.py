# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)]
        while stack:
            curr, total = stack.pop()
            total += curr.val
            
            if not curr.left and not curr.right and total == targetSum:
                return True
            
            if curr.right:
                stack.append((curr.right, total))
                
            if curr.left:
                stack.append((curr.left, total))
        return False

            
            