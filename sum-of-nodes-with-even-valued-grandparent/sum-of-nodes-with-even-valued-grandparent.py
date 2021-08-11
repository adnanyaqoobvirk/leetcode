# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [(root, None, None)]
        current_sum = 0
        while stack:
            current, parent, grandparent = stack.pop()
            if current:
                if grandparent and (grandparent.val % 2 == 0):
                    current_sum += current.val
                stack.append((current.right, current, parent))
                stack.append((current.left, current, parent))
        return current_sum