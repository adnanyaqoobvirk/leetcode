# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = [root]
        while q:
            nq = []
            for node in q:
                node.left, node.right = node.right, node.left
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq
        return root