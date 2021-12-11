# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        def helper(curr: TreeNode) -> None:
            nonlocal successor, foundp
            if curr:
                helper(curr.left)
                
                if not successor and foundp:
                    successor = curr
                else:
                    if curr == p:
                        foundp = True

                    helper(curr.right)
        successor, foundp = None, False
        helper(root)
        return successor