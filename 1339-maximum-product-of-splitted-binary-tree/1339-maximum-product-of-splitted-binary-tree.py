# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def calcNodeSums(curr):
            if not curr:
                return 0
            
            nodeSums[curr] = curr.val + calcNodeSums(curr.left) + calcNodeSums(curr.right)
            return nodeSums[curr]
        
        def getMaxProduct(curr):
            if not curr:
                return 0
            
            return max(
                getMaxProduct(curr.left),
                getMaxProduct(curr.right),
                (nodeSums[root] - nodeSums[curr.left]) * nodeSums[curr.left],
                (nodeSums[root] - nodeSums[curr.right]) * nodeSums[curr.right]
            )
        
        nodeSums = defaultdict(int)
        calcNodeSums(root)
        return getMaxProduct(root) % (10**9 + 7)