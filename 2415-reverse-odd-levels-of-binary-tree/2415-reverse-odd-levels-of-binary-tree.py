# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        lvl = 1
        while q:
            nq = []
            for node in q:
                if node.left:
                    nq.append(node.left)
                    nq.append(node.right)
            if lvl & 1:
                l, r = 0, len(nq) - 1
                while l < r:
                    nq[l].val, nq[r].val = nq[r].val, nq[l].val
                    l += 1
                    r -= 1
            q = nq
            lvl += 1
        return root