# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0, float('inf'), float('-inf') 
            
            left, left_min, left_max = helper(curr.left)
            right, right_min, right_max = helper(curr.right)
        
            if left == -1 or right == -1 or curr.val <= left_max or curr.val >= right_min:
                nodes = -1
            else:
                nodes = 1 + left + right
                nonlocal ans
                ans = max(ans, nodes)
            
            return nodes, min(curr.val, left_min, right_min), max(curr.val, left_max, right_max)
        
        ans = 0
        helper(root)
        return ans
        