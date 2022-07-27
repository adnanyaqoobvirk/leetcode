# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        def helper(curr: Optional[TreeNode]) -> Tuple[TreeNode, TreeNode]:
            tail, left, right = curr, curr.left, curr.right
            
            if left:
                tail.right, tail = helper(left)
            
            curr.left = None
                
            if right:
                tail.right, tail = helper(right)
            
            return curr, tail
        
        helper(root)