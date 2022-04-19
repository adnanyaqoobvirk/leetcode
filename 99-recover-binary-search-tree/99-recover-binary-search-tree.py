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
        stack, head, left, right = [], root, None, None
        while head or stack:
            if head:
                stack.append(head)
                head = head.left
            else:
                curr = stack.pop()
                
                if right:
                    if left.val > curr.val:
                        right = curr
                    else:
                        break
                    
                if not left:
                    left = curr
                elif left.val < curr.val:
                    left = curr
                elif not right:
                    right = curr
                    
                if curr.right:
                    head = curr.right
        left.val, right.val = right.val, left.val