# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        h = 0
        curr = root
        while curr.left:
            curr = curr.left
            h += 1
        
        hcount = 0
        stack = [(root, 1)]
        while stack:
            curr, lvl = stack.pop()
            
            if lvl == h:
                if not curr.left:
                    return 2**h + hcount * 2 - 1
                
                if not curr.right:
                    return 2**h + hcount * 2
                
                hcount += 1
            elif lvl < h:
                stack.append((curr.right, lvl + 1))
                stack.append((curr.left, lvl + 1))
                
        return 2**(h + 1) - 1
        