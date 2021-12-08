# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        stack, successor = [root], TreeNode(float('inf'))
        while stack:
            curr = stack.pop()
            if curr.val > p.val and curr.val < successor.val:
                successor = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return None if successor.val == float('inf') else successor