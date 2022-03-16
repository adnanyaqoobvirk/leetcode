# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.curr = float('-inf')
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.isValidBST(root.left)
        if not left:
            return False
        
        if root.val <= self.curr:
            return False
        
        self.curr = root.val
        
        right = self.isValidBST(root.right)
        if not right:
            return False
        
        return True
        