# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q, ans = [root], []
        while q:
            nq, lvl = [], []
            for node in q:
                lvl.append(node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            ans.append(lvl)
            q = nq
        return ans