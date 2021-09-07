# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def recurse(current: TreeNode) -> TreeNode:
            if current:
                current.left = recurse(current.left)
                current.right = recurse(current.right)
                
                if current.val == target and not current.left and not current.right:
                    return None
                return current
        return recurse(root)
            