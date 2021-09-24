# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, root.val)]
        ans = 0
        while stack:
            current, num = stack.pop()
            if not current.right and not current.left:
                ans += num
            else:
                if current.right:
                    stack.append((current.right, num * 2 + current.right.val))
                if current.left:
                    stack.append((current.left, num * 2 + current.left.val))
        return ans