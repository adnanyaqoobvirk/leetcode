# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack, ans = [(root, 0)], 0
        while stack:
            curr, num = stack.pop()
            num = num * 2 + curr.val
            
            if not curr.left and not curr.right:
                ans += num
            else:
                if curr.right:
                    stack.append((curr.right, num))
                if curr.left:
                    stack.append((curr.left, num))
        return ans
            