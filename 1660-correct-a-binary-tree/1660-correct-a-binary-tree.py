# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        def recurse(current: TreeNode) -> TreeNode:
            if not current or current.right in seen:
                return None
            
            current.right = recurse(current.right)
            current.left = recurse(current.left)
            seen.add(current)
            return current
        
        seen = set()
        return recurse(root)
                
                