# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack, total, nroot = [], 0, root
        while root or stack:
            if root:
                stack.append([root, total])
                root = root.right
            else:
                curr, curr_total = stack.pop()
                curr.val += curr_total
                if stack:
                    stack[-1][1] = curr.val
                total = curr.val
                if curr.left:
                    root = curr.left
        return nroot