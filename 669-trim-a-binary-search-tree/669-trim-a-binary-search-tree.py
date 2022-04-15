# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr:
                return
            
            curr.left = helper(curr.left)
            curr.right = helper(curr.right)
            
            if low > curr.val or curr.val > high:
                if curr.right:
                    if curr.left:
                        prev, ncurr = curr, curr.right
                        while ncurr:
                            prev, ncurr = ncurr, ncurr.left
                        prev.left = curr.left
                    return curr.right
                else:
                    return curr.left
            else:
                return curr
        
        sentinal = TreeNode(val=float('inf'), right=root)
        helper(sentinal)
        return sentinal.right