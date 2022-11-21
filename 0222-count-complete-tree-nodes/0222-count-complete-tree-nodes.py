# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        h = 0
        curr = root
        while curr.left:
            curr = curr.left
            h += 1
        
        def exists(node):
            steps = []
            while node > 1:
                steps.append(True if node & 1 else False)
                node //= 2
        
            curr = root
            for s in reversed(steps):
                curr = curr.right if s else curr.left
            return curr is not None
        
        lo, hi = 2**h, 2**(h + 1)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if exists(mid):
                lo = mid
            else:
                hi = mid
        return lo