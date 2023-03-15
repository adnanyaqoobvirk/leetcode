# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        last_level = False
        while q:
            nq = []
            for curr in q:
                if not last_level:
                    if not curr.left:
                        last_level = True
                        if curr.right:
                            return False
                    else:
                        nq.append(curr.left)

                    if not curr.right:
                        last_level = True
                    else:
                        nq.append(curr.right)
                else:
                    if curr.left or curr.right:
                        return False
            q = nq
        return True
                    
        