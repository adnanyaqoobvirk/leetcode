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
            curr = stack.pop()
            
            if not curr:
                continue
            
            if curr.left in vis and curr.right in vis:
                d = min(vis[curr.left], vis[curr.right])
                vis[curr] = 1 + (0 if d == inf else d)
            else:
                stack.append(curr)
                stack.append(curr.left)
                stack.append(curr.right)
        
        return 0 if vis[root] == inf else vis[root]