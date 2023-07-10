# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q, d = [root], 1
        while q:
            nq = []
            for node in q:
                if not node.left and not node.right:
                    return d
                
                if node.left:
                    nq.append(node.left)
                    
                if node.right:
                    nq.append(node.right)
            q = nq
            d += 1
        return d