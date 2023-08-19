# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return -inf

            left_val = helper(curr.left)
            right_val = helper(curr.right)

            if (left_val == -inf or left_val == curr.val) and (right_val == -inf or right_val == curr.val):
                self.cnt += 1
                return curr.val
            else:
                return inf
        self.cnt = 0
        helper(root)
        return self.cnt
    