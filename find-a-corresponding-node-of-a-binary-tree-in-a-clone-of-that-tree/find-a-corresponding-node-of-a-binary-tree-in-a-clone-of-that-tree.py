# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            ocurrent, ccurrent = stack.pop()
            if ocurrent == target:
                return ccurrent
            if ocurrent.right:
                stack.append((ocurrent.right, ccurrent.right))
            if ocurrent.left:
                stack.append((ocurrent.left, ccurrent.left))