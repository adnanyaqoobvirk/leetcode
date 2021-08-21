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
            last = None
            while stack and stack[-1].val < preorder[i]:
                last = stack.pop()
            
            node = TreeNode(preorder[i])
            if last:
                last.right = node
            else:
                stack[-1].left = node
            stack.append(node)
        return root
            