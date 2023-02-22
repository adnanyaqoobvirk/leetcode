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
        
        sentinal = TreeNode(left = root)
        q = [(root, sentinal, True)]
        while q:
            nq = []
            for curr, parent, left in q:
                if curr.val == key:
                    right = curr.left
                    if curr.right:
                        node = curr.right
                        while node.left:
                            node = node.left
                        node.left = curr.left
                        right = curr.right
                    if left:
                        parent.left = right
                    else:
                        parent.right = right
                    break
                else:
                    if curr.left:
                        nq.append((curr.left, curr, True))
                    if curr.right:
                        nq.append((curr.right, curr, False))
            else:
                q = nq
                continue
            break
        return sentinal.left