# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def recurse(current: TreeNode) -> TreeNode:
            if current:
                if current in nodes_set:
                    return current
                
                left = recurse(current.left)
                right = recurse(current.right)
                if left and right:
                    return current
                return left or right
        
        nodes_set = set(nodes)
        return recurse(root)