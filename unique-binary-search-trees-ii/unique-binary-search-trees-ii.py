# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return [None]
            
            ans = []
            for i in range(lo, hi + 1):
                left = helper(lo, i - 1)
                right = helper(i + 1, hi)
                
                for ltree in left:
                    for rtree in right:
                        ans.append(TreeNode(i, ltree, rtree))
            return ans
        return helper(1, n)