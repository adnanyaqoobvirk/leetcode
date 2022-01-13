# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(i: int, j: int) -> TreeNode:
            if i <= j:
                curr = TreeNode(postorder.pop())
                p = inorder[curr.val]
                curr.right = helper(p + 1, j)
                curr.left = helper(i, p - 1)
                return curr
        inorder = {num: i for i, num in enumerate(inorder)}
        return helper(0, len(inorder) - 1)