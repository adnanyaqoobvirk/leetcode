# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def getTreeHeight(current: TreeNode) -> int:
            if not current:
                return 0
            
            return max(
                getTreeHeight(current.left), 
                getTreeHeight(current.right)
            ) + 1
        
        def recurse(current: TreeNode, h: int) -> int:
            value_sum = 0
            if current:
                if h == height:
                    value_sum += current.val
                value_sum += recurse(current.left, h + 1)
                value_sum += recurse(current.right, h + 1)
            return value_sum
        
        height = getTreeHeight(root)
        return recurse(root, 1)