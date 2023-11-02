# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> Tuple[int, int]:
            if not curr:
                return 0, 0
            
            left_sum, left_count = helper(curr.left)
            right_sum, right_count = helper(curr.right)
            
            total = left_sum + curr.val + right_sum
            count = left_count + 1 + right_count
            avg_val = total // count
            
            if avg_val == curr.val:
                nonlocal ans
                ans += 1
            return total, count
        ans = 0
        helper(root)
        return ans