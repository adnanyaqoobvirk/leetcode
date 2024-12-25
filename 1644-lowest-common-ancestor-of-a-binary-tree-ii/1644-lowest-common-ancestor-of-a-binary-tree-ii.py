# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr: 'TreeNode') -> 'TreeNode':
            if not curr:
                return None

            if curr == p or curr == q:
                seen.add(curr)
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr
            
            if not right:
                if not left:
                    if curr == p or curr == q:
                        return curr
                    else:
                        return None
                else:
                    if curr == p or curr == q:
                        return curr
                    else:
                        return left
            
            if not left:
                if not right:
                    if curr == p or curr == q:
                        return curr
                    else:
                        return None
                else:
                    if curr == p or curr == q:
                        return curr
                    else:
                        return right
            
            return None
        seen = set()
        res = dfs(root)
        if len(seen) == 2:
            return res
        else:
            return None