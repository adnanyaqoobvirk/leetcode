# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recurse(current: TreeNode, maximum: int) -> int:
            if not current:
                return 0
            
            maximum = max(current.val, maximum)
            return (
                int(current.val == maximum) + 
                recurse(current.left, maximum) + 
                recurse(current.right, maximum)
            )
        return recurse(root, float('-inf'))