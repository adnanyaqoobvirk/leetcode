# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack, prev = [], [], None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack[-1]
                if not curr.right or prev == curr.right:
                    ans.append(curr.val)
                    prev = curr
                    stack.pop()
                else:
                    root = curr.right
        return ans