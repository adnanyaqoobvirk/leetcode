# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0
            
            t = dfs(curr.left) + dfs(curr.right) + (curr == p or curr == q)
            
            if t == 2:
                nonlocal ans
                ans = curr
                return 0
                
            return t
        
        ans = None
        dfs(root)
        return ans