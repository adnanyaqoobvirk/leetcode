# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        p = {root: root.val}
        while q:
            nq = []
            total = 0
            for node in q:
                total += node.val

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val

                if node.left:
                    p[node.left] = child_sum
                    nq.append(node.left)
                
                if node.right:
                    p[node.right] = child_sum
                    nq.append(node.right)
            
            for node in q:
                child_sum = p[node]
                node.val = total - child_sum
                
            q = nq
        return root
                
            


        