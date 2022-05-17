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
            onode, cnode = stack.pop()
            if onode == target:
                return cnode
            if onode.right:
                stack.append((onode.right, cnode.right))
            if onode.left:
                stack.append((onode.left, cnode.left))