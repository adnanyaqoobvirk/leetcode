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
                    right = node = curr.right
                    while node.left:
                        node = node.left
                    node.left = curr.left
                    return right
                else:
                    return curr.left
            else:
                curr.left = helper(curr.left)
                curr.right = helper(curr.right)
                return curr
        return helper(root)