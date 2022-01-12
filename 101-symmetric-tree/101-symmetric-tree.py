# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            nq, lvl = [], []
            for node in q:
                if node.left:
                    nq.append(node.left)
                    lvl.append(node.left.val)
                else:
                    lvl.append(-200)
                if node.right:
                    nq.append(node.right)
                    lvl.append(node.right.val)
                else:
                    lvl.append(-200)
            
            left, right = 0, len(lvl) - 1
            while left < right:
                if lvl[left] != lvl[right]:
                    return False
                left += 1
                right -= 1
            q = nq
        return True