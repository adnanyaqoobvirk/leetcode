# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recurse(current: TreeNode, total: int) -> int:
            if not current:
                return total
            
            right = recurse(current.right, total)
            current.val = right + current.val
            return recurse(current.left, current.val)
        
        recurse(root, 0)
        return root