# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def build(left: int, right: int) -> TreeNode:
            if left < right:
                mid = left + (right - left) // 2
                return TreeNode(nodes[mid], build(left, mid), build(mid + 1, right))
                
        nodes = []
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                nodes.append(node.val)
                current = node.right
                
        return build(0, len(nodes))
        
        
        