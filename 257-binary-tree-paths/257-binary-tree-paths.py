# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(curr: Optional[TreeNode]) -> None:
            if not curr.left and not curr.right:
                ans.append("->".join(path))
            else:
                if curr.left:
                    path.append(str(curr.left.val))
                    helper(curr.left)
                    path.pop()
                
                if curr.right:
                    path.append(str(curr.right.val))
                    helper(curr.right)
                    path.pop()
        ans, path = [], [str(root.val)]
        helper(root)
        return ans
        