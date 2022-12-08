# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1_leafs = []
        stack = [root1]
        while stack:
            curr = stack.pop()
            
            if not curr.left and not curr.right:
                r1_leafs.append(curr)
            
            if curr.right:
                stack.append(curr.right)
            
            if curr.left:
                stack.append(curr.left)
                
        stack = [root2]
        i = 0
        while stack:
            curr = stack.pop()
            
            if not curr.left and not curr.right:
                if i >= len(r1_leafs) or r1_leafs[i].val != curr.val:
                    return False
                i += 1
            
            if curr.right:
                stack.append(curr.right)
            
            if curr.left:
                stack.append(curr.left) 
        
        return i == len(r1_leafs)