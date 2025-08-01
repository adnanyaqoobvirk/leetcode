# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        curr, successor = root, None
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                successor = curr
                curr = curr.left
        return successor