# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        
        if not root:
            return node
        
        prev, current = None, root
        while current:
            prev, current = current, current.right if current.val < val else current.left
        
        if prev.val < val:
            prev.right = node
        else:
            prev.left = node
        
        return root