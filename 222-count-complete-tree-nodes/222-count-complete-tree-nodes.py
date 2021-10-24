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
        
        stack = [(root, 1)]
        last_level_nodes = 0
        max_height = 1
        while stack:
            current, height = stack.pop()
            
            if current.right:
                stack.append((current.right, height + 1))
                max_height = max(max_height, height + 1)
            
            if current.left:
                stack.append((current.left, height + 1))
                max_height = max(max_height, height + 1)
                
            if not current.left and not current.right:
                if max_height == height:
                    last_level_nodes += 1
                    
                if current.left:
                    last_level_nodes += 1
                    break
        return last_level_nodes + ((2 ** (max_height - 1)) - 1)