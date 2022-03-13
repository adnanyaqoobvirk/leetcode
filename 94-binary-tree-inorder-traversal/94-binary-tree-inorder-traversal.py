# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(curr: Optional[TreeNode]) -> None:
            if curr:
                helper(curr.left)
                ans.append(curr.val)
                helper(curr.right)
        ans = []
        helper(root)
        return ans