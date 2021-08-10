# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]
        while stack:
            current = stack.pop()
            if current.val == target.val:
                return current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)