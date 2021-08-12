# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        current = root
        total = 0
        while current or stack:
            if current:
                if current.left:
                    stack.append(current.left)
                stack.append(current)
                current = current.right
            else:
                node = stack.pop()
                node.val += total
                total = node.val
                if stack and node.left == stack[-1]:
                    current = stack.pop()
        return root
                
                
                