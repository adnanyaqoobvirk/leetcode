# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def helper(curr: Optional[TreeNode]) -> Tuple[int, int]:
            if not curr:
                return 0, 0
            
            left_sum, left_cnt = helper(curr.left)
            right_sum, right_cnt = helper(curr.right)
            
            curr_sum, curr_cnt = curr.val + left_sum + right_sum, left_cnt + right_cnt + 1
            
            self.avg = max(self.avg, curr_sum / curr_cnt)
            
            return curr_sum, curr_cnt
        
        self.avg = 0
        helper(root)
        return self.avg