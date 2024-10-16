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
                return 0
            
            left = max(dfs(curr.left), 0)
            right = max(dfs(curr.right), 0)

            ans[0] = max(ans[0], curr.val + left + right)

            return max(curr.val + left, curr.val + right)

        ans = [-inf]
        dfs(root)
        return ans[0]