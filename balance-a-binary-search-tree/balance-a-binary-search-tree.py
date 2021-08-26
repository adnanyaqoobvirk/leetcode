# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(current: TreeNode) -> None:
            if current:
                traverse(current.left)
                nodes.append(current.val)
                traverse(current.right)
        
        def build(left: int, right: int) -> TreeNode:
            mid = left + (right - left) // 2
            if left < right:
                node = TreeNode(nodes[mid])
                node.left = build(left, mid)
                node.right = build(mid + 1, right)
                return node
                
        nodes = []
        traverse(root)
        n = len(nodes)
        return build(0, n)
        
        
        