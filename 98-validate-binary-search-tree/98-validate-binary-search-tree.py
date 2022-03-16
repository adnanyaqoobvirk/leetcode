# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(curr: Optional[TreeNode]) -> Tuple[float, float]:
            if not curr:
                return [float('inf'), float('-inf')]
            
            if not curr.left and not curr.right:
                return [curr.val, curr.val]
            
            left_min, left_max = helper(curr.left)
            right_min, right_max = helper(curr.right)
            
            if left_max >= curr.val or right_min <= curr.val:
                return [float('-inf'), float('inf')]
            
            return [min(left_min, right_min, curr.val), max(left_max, right_max, curr.val)]
        
        left, right = helper(root)
        return False if left == float('-inf') and right == float('inf') else True
            