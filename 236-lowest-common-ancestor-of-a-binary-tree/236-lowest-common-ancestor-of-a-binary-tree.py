# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(curr: TreeNode) -> bool:
            nonlocal ans
            
            if not curr: return False
            
            status = curr == p or curr == q
            left, right = helper(curr.left), helper(curr.right)
            
            if (left and right) or (left and status) or (right and status):
                ans = curr
                return False
            return status or left or right
        
        ans = None
        helper(root)
        return ans