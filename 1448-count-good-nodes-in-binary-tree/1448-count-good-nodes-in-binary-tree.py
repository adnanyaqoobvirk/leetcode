# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recurse(current: TreeNode, maximum: int) -> int:
            ans = 0
            if current:
                maximum = max(current.val, maximum)
                if current.val == maximum:
                    ans += 1
                
                ans += recurse(current.left, maximum)
                ans += recurse(current.right, maximum)
            return ans
        return recurse(root, float('-inf'))