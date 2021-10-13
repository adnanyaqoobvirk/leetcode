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
            parent, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                parent = stack.pop()
            
            stack.append(child)
            if child.val > parent.val:
                parent.right = child
            else:
                parent.left = child
        return root