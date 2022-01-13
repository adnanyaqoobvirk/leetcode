# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(i: int, j: int) -> TreeNode:
            for p in range(i, j + 1):
                if inorder[p] == postorder[-1]:
                    curr = TreeNode(postorder.pop())
                    curr.right = helper(p + 1, j)
                    curr.left = helper(i, p - 1)
                    return curr
        return helper(0, len(inorder) - 1)