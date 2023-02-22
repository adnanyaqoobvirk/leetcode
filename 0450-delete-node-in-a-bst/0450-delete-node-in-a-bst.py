# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(curr):
            if not curr:
                return None
            
            if curr.val == key:
                if curr.right:
                    p = curr.right
                    while p.left:
                        p = p.left
                    p.left = curr.left
                    return curr.right
                else:
                    return curr.left
            elif curr.val < key:
                curr.right = helper(curr.right)
            else:
                curr.left = helper(curr.left)
            return curr
        return helper(root)