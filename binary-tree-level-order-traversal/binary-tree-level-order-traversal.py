# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(curr: TreeNode, lvl: int) -> None:
            if curr:
                if len(ans) == lvl:
                    ans.append([])
                ans[lvl].append(curr.val)
                helper(curr.left, lvl + 1)
                helper(curr.right, lvl + 1)
        ans = []
        helper(root, 0)
        return ans