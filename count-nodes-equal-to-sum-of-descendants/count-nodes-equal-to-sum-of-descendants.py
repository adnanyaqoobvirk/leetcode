# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        stack = []
        result = 0
        current = root
        while current or stack:
            if current:
                if current.right:
                    stack.append([current.right, 0])
                stack.append([current,0])
                current = current.left
            else:
                node, total = stack.pop()
                if stack and node.right == stack[-1][0]:
                    current, _ = stack.pop()
                    stack.append([node, total])
                else:
                    if node.val == total:
                        result += 1
                    if stack:
                        stack[-1][1] += total + node.val
        return result