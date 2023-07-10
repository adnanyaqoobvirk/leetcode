# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        stack, vis = [root], {None: inf}
        while stack:
            curr = stack[-1]
            
            if not curr:
                stack.pop()
                continue
            
            if curr.left in vis and curr.right in vis:
                d = min(vis[curr.left], vis[curr.right])
                vis[curr] = 1 + (0 if d == inf else d)
                stack.pop()
            else:
                stack.append(curr.left)
                stack.append(curr.right)
        
        return 0 if vis[root] == inf else vis[root]