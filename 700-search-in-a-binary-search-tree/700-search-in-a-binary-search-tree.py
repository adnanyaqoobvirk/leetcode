# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            current = stack.pop()
            if current.val == val:
                return current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)