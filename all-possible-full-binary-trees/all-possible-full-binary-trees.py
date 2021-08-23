# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cache = {1: [TreeNode()]}
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        elif n in Solution.cache:
            return Solution.cache[n]
        
        fbts = []
        for x in range(1, n, 2):
            for left in self.allPossibleFBT(x):
                for right in self.allPossibleFBT(n - 1 - x):
                    fbts.append(TreeNode(0, left, right))
        Solution.cache[n] = fbts
        return Solution.cache[n]               