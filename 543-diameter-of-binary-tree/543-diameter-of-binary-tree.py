# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(current: TreeNode) -> int:
            if not current:
                return 0
            
            lheight = dfs(current.left)
            rheight = dfs(current.right)
            
            nonlocal d
            d = max(d, lheight + rheight)
            return 1 + max(lheight, rheight)
        d = 0
        dfs(root)
        return d