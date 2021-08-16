# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':  
        if not root:
            return None
        
        nodeMap = {root: NodeCopy()}
        stack = [root]
        while stack:
            current = stack.pop()
            node = nodeMap[current]
            node.val = current.val
            
            if current.right:
                if current.right in nodeMap:
                    node.right = nodeMap[current.right]
                else:
                    node.right = NodeCopy()
                    nodeMap[current.right] = node.right
                stack.append(current.right)
                
            if current.left:
                if current.left in nodeMap:
                    node.left = nodeMap[current.left]
                else:
                    node.left = NodeCopy()
                    nodeMap[current.left] = node.left
                stack.append(current.left)
            
            if current.random:
                if current.random in nodeMap:
                    node.random = nodeMap[current.random]
                else:
                    node.random = NodeCopy()
                    nodeMap[current.random] = node.random
        return nodeMap[root]