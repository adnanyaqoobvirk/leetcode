# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def recurse(minv: int, maxv: int) -> Optional[TreeNode]:
            if not vals or not (minv < vals[-1] < maxv):
                return None

            v = vals.pop()
            return TreeNode(v, recurse(minv, v), recurse(v, maxv))
        vals = preorder[::-1]
        return recurse(0, 1001)