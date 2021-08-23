# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dp = {1: [TreeNode()]}
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        for x in range(3, n + 1, 2):
            fbts = []
            for i in range(1, x, 2):
                for left in Solution.dp[i]:
                    for right in Solution.dp[x - 1 - i]:
                        fbts.append(TreeNode(left=left, right=right))
            Solution.dp[x] = fbts
        return Solution.dp[n]            