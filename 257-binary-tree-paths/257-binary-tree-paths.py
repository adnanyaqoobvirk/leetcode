# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack, ans, path = [root], [], []
        while stack:
            root = stack[-1]
            if path and path[-1] == root:
                stack.pop()
                path.pop()
            else:
                path.append(root)
                if not root.right and not root.left:
                    ans.append("->".join(str(node.val) for node in path))
                else:
                    if root.right:
                        stack.append(root.right)
                    if root.left:
                        stack.append(root.left)
        return ans
                