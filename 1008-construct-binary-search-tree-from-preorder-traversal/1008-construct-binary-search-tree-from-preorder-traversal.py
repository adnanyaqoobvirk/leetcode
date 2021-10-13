# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            parent = stack[-1]
            while stack and stack[-1].val < preorder[i]:
                parent = stack.pop()
            
            if preorder[i] > parent.val:
                parent.right = TreeNode(preorder[i])
                stack.append(parent.right)
            else:
                parent.left = TreeNode(preorder[i])
                stack.append(parent.left)
        return root