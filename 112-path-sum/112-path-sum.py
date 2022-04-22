# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack, path = [root], []
        while stack:
            root = stack[-1]
            if path and path[-1][0] == root:
                if path[-1][1] == targetSum and not root.right and not root.left:
                    return True
                path.pop()
                stack.pop()
            else:
                path.append((root, root.val + (path[-1][1] if path else 0)))
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return False