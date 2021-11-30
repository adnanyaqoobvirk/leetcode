# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        null = [0, float('inf'), float('-inf')]
        ans, stack, done = 0, [root], {}
        while stack:
            curr = stack[-1]

            if curr not in done:
                if curr.right:
                    stack.append(curr.right)

                if curr.left:
                    stack.append(curr.left)
                done[curr] = null
            else:
                stack.pop()
                
                left, left_min, left_max = done[curr.left] if curr.left else null
                right, right_min, right_max = done[curr.right] if curr.right else null

                if left == -1 or right == -1 or curr.val <= left_max or curr.val >= right_min:
                    nodes = -1
                else:
                    nodes = 1 + left + right
                    ans = max(ans, nodes)

                done[curr] = [nodes, min(curr.val, left_min, right_min), max(curr.val, left_max, right_max)]
        return ans