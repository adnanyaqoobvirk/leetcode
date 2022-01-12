# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(curr: TreeNode) -> None:
            if curr:
                helper(curr.left)
                helper(curr.right)
                ans.append(curr.val)
        ans = []
        helper(root)
        return ans