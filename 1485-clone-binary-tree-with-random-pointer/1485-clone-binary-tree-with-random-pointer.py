# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def helper(curr):
            if not curr:
                return None
            
            if curr not in node_map:
                node_map[curr] = NodeCopy(curr.val)
                
            node_map[curr].left = helper(curr.left)
            node_map[curr].right = helper(curr.right)
            
            if curr.random not in node_map:
                node_map[curr.random] = NodeCopy(curr.random.val)
                
            node_map[curr].random = node_map[curr.random]
            return node_map[curr]
        node_map = {None: None}
        return helper(root)