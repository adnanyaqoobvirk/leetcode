# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        q = [root]
        while q:
            nq = []
            for i in range(len(q)):
                node = q[i]
                if node == u:
                    if i + 1 < len(q):
                        return q[i + 1]
                    else:
                        return None
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq