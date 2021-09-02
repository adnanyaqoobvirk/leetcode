# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(current: TreeNode) -> int:
            if current:
                yield from inorder(current.left)
                yield current.val
                yield from inorder(current.right)
        
        sentinal = current = TreeNode()
        for val in inorder(root):
            current.right = TreeNode(val)
            current = current.right
        return sentinal.right
                