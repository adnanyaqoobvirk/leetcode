# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def recurse(current: TreeNode, parent: TreeNode, grandparent: TreeNode) -> int:
            current_sum = 0
            if current:
                if grandparent and (grandparent.val % 2 == 0):
                    current_sum += current.val
                current_sum += recurse(
                        current.left, current, parent
                    ) + recurse(
                        current.right, current, parent
                    )
            return current_sum
        return recurse(root, None, None)