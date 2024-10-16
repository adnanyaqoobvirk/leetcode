# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = [root] if root else []
        while q:
            nq = []
            lvl = []
            for node in q:
                lvl.append(node.val)
                
                if node.left:
                    nq.append(node.left)
                
                if node.right:
                    nq.append(node.right)
            q = nq
            ans.append(lvl)
        return reversed(ans)