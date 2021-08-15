# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = [root]
        while stack:
            current = stack.pop()
            if current.left and current.right:
                stack.append(current.right)
                stack.append(current.left)
            elif current.left:
                stack.append(current.left)
                output.append(current.left.val)
            elif current.right:
                stack.append(current.right)
                output.append(current.right.val)
        return output
                