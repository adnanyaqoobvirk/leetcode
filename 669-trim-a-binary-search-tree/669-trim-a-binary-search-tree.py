# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr: 
                return
            elif curr.val > high:
                return helper(curr.left)
            elif curr.val < low:
                return helper(curr.right)
            else:
                curr.left = helper(curr.left)
                curr.right = helper(curr.right)
                return curr
        return helper(root)