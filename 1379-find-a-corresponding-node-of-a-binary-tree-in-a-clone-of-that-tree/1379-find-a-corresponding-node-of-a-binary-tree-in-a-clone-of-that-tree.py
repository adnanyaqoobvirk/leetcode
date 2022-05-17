# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        root, found = (original, cloned), None
        while root[0]:
            if root[0].left:
                onode, cnode = root[0].left, root[1].left
                while onode.right and onode.right != root[0]:
                    onode, cnode = onode.right, cnode.right
                    
                if not onode.right:
                    if root[0] == target:
                        found = root[1]
                    onode.right, cnode.right = root[0], root[1]
                    root = (root[0].left, root[1].left)
                else:
                    onode.right, cnode.right = None, None
                    root = (root[0].right, root[1].right)
            else:
                if root[0] == target:
                    found = root[1]
                root = (root[0].right, root[1].right)
        return found