# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(current: TreeNode) -> None:
            if current:
                inorder(current.left)
                nodes.append(current.val)
                inorder(current.right)
        
        nodes = []
        inorder(root)
        
        nroot = None
        current = None
        for node in nodes:
            nnode = TreeNode(node)
            if not nroot:
                current = nroot = nnode
            else:
                current.right = nnode
                current = current.right
        return nroot
                