# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(lo, hi):
            nonlocal idx
            if lo > hi:
                return None
            
            val = preorder[idx]
            mid = inorder_map[val]
            idx += 1
            return TreeNode(val, helper(lo, mid - 1), helper(mid + 1, hi))
        n = len(preorder)
        idx = 0
        inorder_map = {v: i for i, v in enumerate(inorder)}
        return helper(0, n - 1)