# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = [(None, root, True)]
        while q:
            nq = []
            seen = set()
            for parent, node, right in q:
                if node.right in seen:
                    if right:
                        parent.right = None
                    else:
                        parent.left = None
                    return root
                seen.add(node)
                if node.right:
                    nq.append((node, node.right, True))
                if node.left:
                    nq.append((node, node.left, False))
            q = nq
        return root
                
                