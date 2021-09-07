# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = []
        current = root
        while current or stack:
            if current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                if stack and node.right == stack[-1]:
                    current = stack.pop()
                    stack.append(node)
                else:
                    if node.left is None and node.right is None and node.val == target:
                        if stack:
                            if stack[-1].left == node:
                                stack[-1].left = None
                            else:
                                stack[-1].right = None
                        else:
                            return None
        return root