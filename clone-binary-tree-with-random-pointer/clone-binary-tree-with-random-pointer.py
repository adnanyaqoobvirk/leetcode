# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        def recurse(current: Node) -> NodeCopy:
            if current:
                if current in nodeMap:
                    node = nodeMap[current]
                    node.val = current.val
                else:
                    node = NodeCopy(current.val)
                    
                nodeMap[current] = node
                node.left = recurse(current.left)
                node.right = recurse(current.right)
                
                if current.random:
                    if current.random in nodeMap:
                        node.random = nodeMap[current.random]
                    else:
                        node.random = NodeCopy()
                        nodeMap[current.random] = node.random
                return node
                
        nodeMap = {}
        return recurse(root)