# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                curr = root.left
                while curr.right and curr.right != root:
                    curr = curr.right
                
                if not curr.right:
                    curr.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    curr.right = None
                    root = root.right
        return res