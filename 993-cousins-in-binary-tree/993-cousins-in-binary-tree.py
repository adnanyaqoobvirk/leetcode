# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        while q:
            nq = []
            xparent = yparent = None
            for node in q:
                if node.left:
                    nq.append(node.left)
                    
                    if node.left.val == x:
                        xparent = node
                    elif node.left.val == y:
                        yparent = node
                
                if node.right:
                    nq.append(node.right)
                    
                    if node.right.val == x:
                        xparent = node
                    elif node.right.val == y:
                        yparent = node
            if xparent and yparent and xparent != yparent:
                return True
            q = nq
        return False