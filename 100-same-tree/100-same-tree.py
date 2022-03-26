# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            curr_p, curr_q = stack.pop()
            if not curr_p:
                if curr_q:
                    return False
            elif not curr_q:
                if curr_p:
                    return False
            else:
                if curr_p.val != curr_q.val:
                    return False
                
                stack.append((curr_p.right, curr_q.right))
                stack.append((curr_p.left, curr_q.left))
        return True