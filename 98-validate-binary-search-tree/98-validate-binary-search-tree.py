# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minimum: int = float('-inf'), maximum: int = float('inf')) -> bool:
            if not root:
                return True
            
            if root.val <= minimum or root.val >= maximum:
                return False
            
            return self.isValidBST(root.left, minimum, root.val) and self.isValidBST(root.right, root.val, maximum)