# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(curr: TreeNode, num: int) -> None:
            if curr:
                num = num * 2 + curr.val
                if not curr.left and not curr.right:
                    nonlocal ans
                    ans += num
                else:
                    helper(curr.left, num)
                    helper(curr.right, num)
        ans = 0
        helper(root, 0)
        return ans