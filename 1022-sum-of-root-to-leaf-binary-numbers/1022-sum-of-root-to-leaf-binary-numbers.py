# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def recurse(current: TreeNode, num: int) -> int:
            if not current:
                return 0
            
            num = num * 2 + current.val
            
            if not current.left and not current.right:
                return num
            
            return recurse(current.left, num) + recurse(current.right, num)
        
        return recurse(root, 0)