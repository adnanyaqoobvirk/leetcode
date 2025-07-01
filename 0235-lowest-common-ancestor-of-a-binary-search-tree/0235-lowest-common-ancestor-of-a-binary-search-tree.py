# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(curr: 'TreeNode') -> 'TreeNode':
            if not curr:
                return None
            
            left, right = recurse(curr.left), recurse(curr.right)
        
            if curr == p or curr == q or (left and right):
                return curr
            
            return left or right
        return recurse(root)