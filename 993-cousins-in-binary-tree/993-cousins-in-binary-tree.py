# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(current: TreeNode, parent: TreeNode, depth: int) -> None:
            nonlocal xparent, yparent, xdepth, ydepth
            
            if current:
                if current.val == x:
                    xparent, xdepth = parent, depth
                elif current.val == y:
                    yparent, ydepth = parent, depth
                
                dfs(current.left, current, depth + 1)
                dfs(current.right, current, depth + 1)
        
        xparent = yparent = xdepth = ydepth = None
        dfs(root, None, 0)
        return xparent != yparent and xdepth == ydepth