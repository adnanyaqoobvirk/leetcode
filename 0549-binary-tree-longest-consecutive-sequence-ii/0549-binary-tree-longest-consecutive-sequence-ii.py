# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(curr: TreeNode) -> Tuple[int, int]:
            if not curr:
                return (0, 0)
            
            nonlocal ans
            
            left_pmax, left_nmax = helper(curr.left)
            right_pmax, right_nmax = helper(curr.right)
            
            if curr.left and curr.right and (curr.left.val == curr.val - 1 and curr.right.val == curr.val + 1):
                ans = max(ans, left_nmax + right_pmax + 1)
            
            if curr.left and curr.right and (curr.left.val == curr.val + 1 and curr.right.val == curr.val - 1):
                ans = max(ans, left_pmax + right_nmax + 1)
                
            if curr.left and curr.left.val == curr.val + 1:
                left_pmax += 1
            else:
                left_pmax = 1
            
            if curr.left and curr.left.val == curr.val - 1:
                left_nmax += 1
            else:
                left_nmax = 1
            
            if curr.right and curr.right.val == curr.val + 1:
                right_pmax += 1
            else:
                right_pmax = 1
            
            if curr.right and curr.right.val == curr.val - 1:
                right_nmax += 1
            else:
                right_nmax = 1
            
            ans = max(ans, left_pmax, left_nmax, right_pmax, right_nmax)
            
            return (max(left_pmax, right_pmax), max(left_nmax, right_nmax))
        
        ans = 1
        helper(root)
        return ans