# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        
        def helper(curr):
            if not curr:
                return 0
            
            counts[curr.val] += 1
            
            return max(counts[curr.val], helper(curr.left), helper(curr.right))
        
        max_count = helper(root)
        
        return [k for k, v in counts.items() if v == max_count]