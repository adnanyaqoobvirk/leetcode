# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recurse(current: TreeNode) -> Tuple[int, int]:
            nonlocal max_diff
            
            if not current:
                return float('inf'), float('-inf')
            
            left_min, left_max = recurse(current.left)
            right_min, right_max = recurse(current.right)
            
            child_min, child_max = min(left_min, right_min), max(left_max, right_max)
            
            if child_min != float('inf'):
                max_diff = max(abs(current.val - child_min), max_diff)
            
            if child_max != float('-inf'):
                max_diff = max(abs(current.val - child_max), max_diff)
                
            return min(current.val, child_min), max(current.val, child_max)
        
        max_diff = 0
        recurse(root)
        return max_diff