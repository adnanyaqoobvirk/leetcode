# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = [root]
        while q:
            new_q = []
            for current in q:
                if current.left:
                    new_q.append(current.left)
                if current.right:
                    new_q.append(current.right)
            if new_q:
                q = new_q
            else:
                return sum(current.val for current in q)