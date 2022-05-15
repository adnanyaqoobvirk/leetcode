# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            nq, total = [], 0
            for node in q:
                total += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            if not nq:
                return total
            q = nq