# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return -1
        
            left, right = helper(curr.left), helper(curr.right)
            
            h = max(left, right) + 1
            
            if len(ans) <= h:
                ans.append([])
                
            ans[h].append(curr.val)
            
            return h
        ans = []
        helper(root)
        return ans