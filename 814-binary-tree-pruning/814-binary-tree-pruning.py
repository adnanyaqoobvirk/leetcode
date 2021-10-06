# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(current: TreeNode) -> bool:
            if not current:
                return False
            
            left = recurse(current.left)
            right = recurse(current.right)
            if not left:
                current.left = None
            if not right:
                current.right = None
            
            return bool(current.val) | left | right
        
        return root if recurse(root) else None