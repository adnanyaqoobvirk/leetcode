# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(curr: TreeNode) -> Tuple[int, int]:
            if not curr:
                return 0, 0

            if not curr.left and not curr.right:
                return 1, curr.val

            left_cnt, left_val = helper(curr.left)
            right_cnt, right_val = helper(curr.right)

            if curr.left and curr.right:
                if curr.val == left_val == right_val:
                    return 1 + left_cnt + right_cnt, curr.val
            elif curr.left and curr.val == left_val:
                return 1 + left_cnt, curr.val
            elif curr.right and curr.val == right_val:
                return 1 + right_cnt, curr.val

            return left_cnt + right_cnt, -2000
        return helper(root)[0]