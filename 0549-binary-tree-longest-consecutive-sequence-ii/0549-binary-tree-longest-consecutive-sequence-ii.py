# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(curr: Optional[TreeNode]) -> Tuple[int, int]:
            if not curr:
                return 0, 0
            
            left_inc, left_dec = dfs(curr.left)
            right_inc, right_dec = dfs(curr.right)
        
            curr_inc = 1
            curr_dec = 1
            if curr.left:
                if curr.val == curr.left.val + 1:
                    curr_dec = max(curr_dec, left_dec + 1)
                elif curr.val == curr.left.val - 1:
                    curr_inc = max(curr_inc, left_inc + 1)
            
            if curr.right:
                if curr.val == curr.right.val + 1:
                    curr_dec = max(curr_dec, right_dec + 1)
                elif curr.val == curr.right.val - 1:
                    curr_inc = max(curr_inc, right_inc + 1)

            max_length[0] = max(max_length[0], curr_inc + curr_dec - 1)
            return curr_inc, curr_dec
        
        max_length = [0]
        dfs(root)
        return max_length[0]