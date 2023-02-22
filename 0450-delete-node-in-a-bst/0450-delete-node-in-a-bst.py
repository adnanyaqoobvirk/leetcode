# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        def delete(node):
            if node.right:
                p = node.right
                while p.left:
                    p = p.left
                p.left = node.left
                return node.right
            else:
                return node.left
        
        if root.val == key:
            return delete(root)
        
        q = [root]
        while q:
            nq = []
            for curr in q:
                if curr.left:
                    if curr.left.val == key:
                        curr.left = delete(curr.left)
                        return root
                    nq.append(curr.left)
                if curr.right:
                    if curr.right.val == key:
                        curr.right = delete(curr.right)
                        return root
                    nq.append(curr.right)
            q = nq
        return root