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
        
        if h == 0:
            return 1
        
        def exists(node):
            left, right, curr = 0, 2**h - 1, root
            for _ in range(h):
                mid = (left + right) // 2
                if node <= mid:
                    curr = curr.left
                    right = mid
                else:
                    curr = curr.right
                    left = mid + 1
            return curr is not None
        
        l, r = 1, 2**h - 1
        while l <= r:
            m = (l + r) // 2
            if exists(m):
                l = m + 1
            else:
                r = m - 1
                
        return 2**h - 1 + l
                