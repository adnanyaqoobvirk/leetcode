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
                return 0, 0
            
            nonlocal ans
            
            left_pmax, left_nmax = (v + 1 for v in helper(curr.left))
            right_pmax, right_nmax = (v + 1 for v in helper(curr.right))
            
            if curr.left and curr.right:
                if curr.left.val == curr.val - 1 and curr.right.val == curr.val + 1:
                    ans = max(ans, left_nmax + right_pmax - 1)
            
                if curr.left.val == curr.val + 1 and curr.right.val == curr.val - 1:
                    ans = max(ans, left_pmax + right_nmax - 1)
            
            if curr.left:
                if curr.left.val != curr.val + 1:
                    left_pmax = 1

                if curr.left.val != curr.val - 1:
                    left_nmax = 1
            
            if curr.right:
                if curr.right.val != curr.val + 1:
                    right_pmax = 1

                if curr.right.val != curr.val - 1:
                    right_nmax = 1
            
            pmax, nmax = max(left_pmax, right_pmax), max(left_nmax, right_nmax)
            ans = max(ans, pmax, nmax)
            
            return pmax, nmax
        
        ans = 1
        helper(root)
        return ans