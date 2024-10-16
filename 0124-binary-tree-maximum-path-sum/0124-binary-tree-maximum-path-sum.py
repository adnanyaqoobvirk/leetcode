# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return -inf
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            ans[0] = max(ans[0], curr.val + left + right, left, right)

            return max(curr.val + left, curr.val + right, curr.val)

        ans = [-inf]
        return max(dfs(root), ans[0])