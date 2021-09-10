# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        while root.left or root.right:
            stack = [root]
            leafs = []
            while stack:
                current = stack.pop()
                if current.left:
                    if not current.left.left and not current.left.right:
                        leafs.append(current.left.val)
                        current.left = None
                    else:
                        stack.append(current.left)
                
                if current.right:
                    if not current.right.left and not current.right.right:
                        leafs.append(current.right.val)
                        current.right = None
                    else:
                        stack.append(current.right)
            if leafs:
                ans.append(leafs)
        ans.append([root.val])
        return ans
                    