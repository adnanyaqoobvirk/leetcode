# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = diff = inf
        stack = [root]
        while stack:
            curr = stack.pop()
            
            if not curr:
                continue
                
            curr_diff = abs(curr.val - target)
            if curr_diff == diff:
                closest = min(closest, curr.val)
            elif curr_diff < diff:
                closest = curr.val
                
            diff = min(diff, curr_diff)
            
            stack.append(curr.right)
            stack.append(curr.left)
        return closest