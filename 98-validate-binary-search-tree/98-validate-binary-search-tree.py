# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr, stack, prev = root, [], float('-inf')
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if node.val <= prev:
                    return False
                prev = node.val
                curr = node.right
        return True    
            
        