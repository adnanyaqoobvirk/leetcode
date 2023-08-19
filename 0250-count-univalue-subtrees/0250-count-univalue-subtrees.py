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
                return 1001, 0
            
            if not curr.left and not curr.right:
                return curr.val, 1
            elif not curr.left:
                right_val, right_cnt = helper(curr.right)
                if right_val == curr.val:
                    return curr.val, right_cnt + 1
                else:
                    return 1001, right_cnt
            elif not curr.right:
                left_val, left_cnt = helper(curr.left)
                if left_val == curr.val:
                    return curr.val, left_cnt + 1
                else:
                    return 1001, left_cnt
            else:
                left_val, left_cnt = helper(curr.left)
                right_val, right_cnt = helper(curr.right)
            
                if left_val == right_val == curr.val:
                    return curr.val, left_cnt + right_cnt + 1
                else:
                    return 1001, left_cnt + right_cnt
        return helper(root)[1]
    