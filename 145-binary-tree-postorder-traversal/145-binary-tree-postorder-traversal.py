# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        while root or stack:
            if root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                if stack and stack[-1] == curr.right:
                    root = stack.pop()
                    stack.append(curr)
                else:
                    ans.append(curr.val)
        return ans