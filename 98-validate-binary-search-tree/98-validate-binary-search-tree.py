# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minimum: int = float('-inf'), maximum: int = float('inf')) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            curr, minimum, maximum = stack.pop()
            
            if curr.val <= minimum or curr.val >= maximum:
                return False
            
            if curr.right:
                stack.append((curr.right, curr.val, maximum))
            
            if curr.left:
                stack.append((curr.left, minimum, curr.val))
        return True