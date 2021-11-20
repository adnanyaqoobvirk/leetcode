# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(current: TreeNode) -> Tuple[int, bool]:
            nonlocal count

            if not current:
                return (None, True)
            
            left, luni = helper(current.left)
            right, runi = helper(current.right)

            uni = True
            if left and current.val != left:
                uni = False

            if right and current.val != right:
                uni = False

            if uni and luni and runi:
                count += 1

            return (current.val, uni and luni and runi)

        count = 0
        helper(root)
        return count