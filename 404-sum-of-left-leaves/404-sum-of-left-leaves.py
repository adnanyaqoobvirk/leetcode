# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        ans = 0
        while stack:
            current = stack.pop()
            
            if current.right:
                stack.append(current.right)
                
            if current.left:
                if not current.left.left and not current.left.right:
                    ans += current.left.val
                else:
                    stack.append(current.left)
        return ans