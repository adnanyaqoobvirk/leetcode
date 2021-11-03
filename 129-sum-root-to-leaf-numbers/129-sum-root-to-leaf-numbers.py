# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(current: TreeNode, number: int) -> None:
            if current:
                number = number * 10 + current.val 
                if not current.left and not current.right:
                    nonlocal total
                    total += number
                else:
                    helper(current.left, number)
                    helper(current.right, number)
        
        total = 0
        helper(root, 0)
        return total