# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(current: TreeNode) -> TreeNode:
            if not current:
                return None
            
            if current.val == key:
                if current.right:
                    if current.left:
                        node = current.right
                        while node.left:
                            node = node.left
                        node.left = current.left
                    return current.right
                elif current.left:
                    return current.left
                else:
                    return None
            elif current.val > key:
                current.left = helper(current.left)
            else:
                current.right = helper(current.right)
            
            return current
        return helper(root)