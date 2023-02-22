# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(lo, hi):
            if lo > hi:
                return None
            val = postorder.pop()
            mid = inorder_map[val]
            return TreeNode(val, right = helper(mid + 1, hi), left = helper(lo, mid - 1))
        inorder_map = {v: i for i, v in enumerate(inorder)}
        return helper(0, len(postorder) - 1)