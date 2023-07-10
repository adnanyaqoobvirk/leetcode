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
        
        def helper(curr: TreeNode) -> int:
            if not curr:
                return inf
            
            if not curr.left and not curr.right:
                return 1
            
            return 1 + min(helper(curr.left), helper(curr.right))
        return helper(root)