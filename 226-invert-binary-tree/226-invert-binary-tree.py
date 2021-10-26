# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            current = stack.pop()
            
            current.left, current.right = current.right, current.left
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return root