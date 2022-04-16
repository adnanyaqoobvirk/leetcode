# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(curr: Optional[TreeNode], total: int) -> int:
            if not curr:
                return total
            
            right_total = helper(curr.right, total)
            curr.val += right_total
            return helper(curr.left, curr.val)
        helper(root, 0)
        return root