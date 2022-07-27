# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.right:
                if curr.left:
                    pre = curr.left
                    while pre.right:
                        pre = pre.right
                    pre.right = curr.right

                    curr.right = curr.left
                    curr.left = None
                curr = curr.right
            else:
                curr.right = curr.left
                curr.left = None
                curr = curr.right