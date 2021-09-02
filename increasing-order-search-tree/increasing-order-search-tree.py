# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sentinal = self.current = TreeNode()
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(current: TreeNode) -> int:
            if current:
                inorder(current.left)
                current.left = None
                self.current.right = current
                self.current = self.current.right
                inorder(current.right)
        inorder(root)
        return self.sentinal.right
                