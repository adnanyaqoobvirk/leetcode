# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        vals, stack, head = [], [], root
        while head or stack:
            if head:
                stack.append(head)
                head = head.left
            else:
                curr = stack.pop()
                vals.append(curr.val)
                if curr.right:
                    head = curr.right
        
        vals.sort()
        
        head = root
        while head or stack:
            if head:
                stack.append(head)
                head = head.right
            else:
                curr = stack.pop()
                curr.val = vals.pop()
                if curr.left:
                    head = curr.left