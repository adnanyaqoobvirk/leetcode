# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [(root, 0)]
        xparent = yparent = xdepth = ydepth = None
        
        while stack:
            current, depth = stack.pop()
            
            ndepth = depth + 1
            if current.left:
                stack.append((current.left, ndepth))
                
                if current.left.val == x:
                    xparent, xdepth = current, ndepth
                elif current.left.val == y:
                    yparent, ydepth = current, ndepth
            
            if current.right:
                stack.append((current.right, ndepth))
                
                if current.right.val == x:
                    xparent, xdepth = current, ndepth
                elif current.right.val == y:
                    yparent, ydepth = current, ndepth
        
        return xparent != yparent and xdepth == ydepth