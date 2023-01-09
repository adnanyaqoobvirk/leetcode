# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                
                if not pre.right:
                    ans.append(root.val)
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    root = root.right
            else:
                ans.append(root.val)
                root = root.right
        return ans