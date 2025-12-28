# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                
                if pre.right and pre.right == root:
                    result.append(pre.right.val)
                    pre.right = None
                    root = root.right
                else:
                    pre.right = root
                    root = root.left
        return result