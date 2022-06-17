# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def helper(curr: TreeNode, parent: TreeNode) -> int:
            if not curr:
                return 0
            
            ans = 0
            ans += helper(curr.left, curr)
            ans += helper(curr.right, curr)
            
            if curr.left not in covered or curr.right not in covered or (
                curr not in covered and not parent
            ):
                ans += 1
                covered.add(curr.left)
                covered.add(curr.right)
                covered.add(curr)
                covered.add(parent)
        
            return ans
        covered = {None}
        return helper(root, None)