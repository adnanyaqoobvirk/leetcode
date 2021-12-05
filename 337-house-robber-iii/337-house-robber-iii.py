# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        childs_money = 0
        if root.left:
            childs_money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            childs_money += self.rob(root.right.left) + self.rob(root.right.right)
            
        return max(
            root.val + childs_money,
            self.rob(root.left) + self.rob(root.right)
        )