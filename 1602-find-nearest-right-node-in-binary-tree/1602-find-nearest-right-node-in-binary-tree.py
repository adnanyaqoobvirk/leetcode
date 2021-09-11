# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def recurse(current: TreeNode, depth: int) -> TreeNode:
            nonlocal target
            if current:
                if target == depth:
                    return current
                
                if current == u:
                    target = depth
                else:
                    return recurse(current.left, depth + 1) or recurse(current.right, depth + 1)
        target = -1
        return recurse(root, 0)