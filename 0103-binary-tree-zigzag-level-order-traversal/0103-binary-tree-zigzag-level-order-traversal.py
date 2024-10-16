# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = [root] if root else []
        reverse = False
        while q:
            nq = []
            lvl = []
            for node in reversed(q) if reverse else q:
                lvl.append(node.val)

                if node.left:
                    nq.append(node.left)
                
                if node.right:
                    nq.append(node.right)

            reverse = not reverse
            q = nq
            ans.append(lvl)
        return ans   