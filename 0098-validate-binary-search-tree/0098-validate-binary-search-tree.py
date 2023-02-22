# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -inf
        curr = root
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if prev >= node.val:
                    return False
                prev = node.val
                curr = node.right
        return True
                