# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            ans = 0
            if low <= curr.val <= high:
                ans += curr.val
            
            if curr.val < high:
                ans += helper(curr.right)
            
            if curr.val > low:
                ans += helper(curr.left)
            
            return ans
        return helper(root)