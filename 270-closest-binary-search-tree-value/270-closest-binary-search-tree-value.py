# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack, min_diff, ans = [root], float('inf'), None
        while stack:
            curr = stack.pop()
            curr_diff = abs(target - curr.val)
            if curr_diff < min_diff:
                min_diff, ans = curr_diff, curr.val
                
            if curr.right:
                stack.append(curr.right)
            
            if curr.left:
                stack.append(curr.left)
        return ans
            