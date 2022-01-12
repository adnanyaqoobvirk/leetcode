# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(curr: TreeNode) -> None:
            if curr:
                ans.append(curr.val)
                helper(curr.left)
                helper(curr.right)
        ans = []
        helper(root)
        return ans