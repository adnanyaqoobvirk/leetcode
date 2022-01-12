# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, ans = [(root, False)], []
        while stack:
            curr, done = stack.pop()
            if done:
                ans.append(curr.val)
            else:
                if curr.right:
                    stack.append((curr.right, False))
                stack.append((curr, True))
                if curr.left:
                    stack.append((curr.left, False))
        return ans