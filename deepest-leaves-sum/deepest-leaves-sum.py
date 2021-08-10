# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_height = 0
        value_sum = 0
        while stack:
            current, current_height = stack.pop()
            if not current.left and not current.right:
                if current_height > max_height:
                    value_sum = current.val
                    max_height = current_height
                elif current_height == max_height:
                    value_sum += current.val
            else:
                if current.right:
                    stack.append((current.right, current_height + 1))
                if current.left:
                    stack.append((current.left, current_height + 1))
        return value_sum