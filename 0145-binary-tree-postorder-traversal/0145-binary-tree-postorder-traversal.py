# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if not root.right:
                res.append(root.val)
                root = root.left
            else:
                curr = root.right
                while curr.left and curr.left != root:
                    curr = curr.left
                
                if not curr.left:
                    curr.left = root
                    res.append(root.val)
                    root = root.right
                else:
                    curr.left = None
                    root = root.left
        return res[::-1]