# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = []
        found = False
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                if found:
                    return curr
                if curr == p:
                    found = True                
                root = curr.right
        return None