# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack, curr, ans, depth = [], root, 0, 0
        while curr or stack:
            if curr:
                depth += 1
                ans = max(ans, depth)
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                depth -= 1
                node = stack.pop()
                if stack and node.right == stack[-1]:
                    depth += 1
                    curr = stack.pop()
                    stack.append(node)
        return ans