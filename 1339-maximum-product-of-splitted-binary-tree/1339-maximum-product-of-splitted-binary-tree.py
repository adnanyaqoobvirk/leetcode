# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            total += curr.val
            stack.append(curr.left)
            stack.append(curr.right)
        
        max_product = 0
        node_sums = defaultdict(int)
        stack = [(root, False)]
        while stack:
            curr, done = stack.pop()

            if done:
                node_sums[curr] = node_sums[curr.left] + node_sums[curr.right] + curr.val
                max_product = max(max_product, (total - node_sums[curr]) * node_sums[curr])
            else:
                stack.append((curr, True))
                if curr.right:
                    stack.append((curr.right, False))
                if curr.left:
                    stack.append((curr.left, False))
        return max_product % (10**9 + 7)