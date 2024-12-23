# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def countSwaps(nodes: List[TreeNode]) -> int:
            if not nodes:
                return 0

            res = 0
            indexes = {v: i for i, v in enumerate(nodes)}
            snodes = sorted(nodes)
            for i, v in enumerate(snodes):
                j = indexes[v]
                if i != j:
                    res += 1
                    indexes[nodes[j]], indexes[nodes[i]] = i, j
            return res

        ans = 0
        q = [root]
        while q:
            nq = []
            vals = []
            for node in q:
                if node.left:
                    nq.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    nq.append(node.right)
                    vals.append(node.right.val)
            ans += countSwaps(vals)
            q = nq
        return ans