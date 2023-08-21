# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> Tuple[int, int, int]:
            if not curr:
                return [0, inf, -inf]
            
            left_count, left_min, left_max = helper(curr.left)
            right_count, right_min, right_max = helper(curr.right)
            
            if left_count > 0 and left_max >= curr.val:
                return [inf, -inf, inf]
            
            if right_count > 0 and right_min <= curr.val:
                return [inf, -inf, inf]
            
            count = left_count + right_count + 1
            self.largest = max(self.largest, count)
            
            return count, min(left_min, curr.val), max(right_max, curr.val)
        
        self.largest = 0
        helper(root)
        return self.largest