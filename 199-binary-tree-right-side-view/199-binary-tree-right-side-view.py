# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = [root]
        ans = []
        while q:
            ans.append(q[-1].val)
            
            nq = []
            for curr in q:
                if curr.left:
                    nq.append(curr.left)
                if curr.right:
                    nq.append(curr.right)
            q = nq
        return ans