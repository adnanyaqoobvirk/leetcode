# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def recurse(current: TreeNode) -> int:
            if not current:
                return 0
            
            i = max(recurse(current.left), recurse(current.right))
            if len(ans) < (i + 1):
                ans.append([])
            ans[i].append(current.val)

            return i + 1
                
        ans = []
        recurse(root)
        return ans