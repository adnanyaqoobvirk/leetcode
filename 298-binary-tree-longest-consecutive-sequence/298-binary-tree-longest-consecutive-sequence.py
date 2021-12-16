# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> int:
            nonlocal max_seq
            
            if not curr:
                return 0

            left = helper(curr.left)
            right = helper(curr.right)

            ans = 1
            if curr.left and curr.left.val - 1 == curr.val:
                ans = left + 1 

            if curr.right and curr.right.val - 1 == curr.val:
                ans = max(ans, right + 1)
                
            max_seq = max(max_seq, ans)
            return ans
        
        max_seq = 0
        helper(root)
        return max_seq