# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def sort(root: TreeNode) -> List[int]:
            result = []
            stack = []
            current = root
            while current or stack:
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    node = stack.pop()
                    result.append(node.val)
                    current = node.right
            return result
                    
        
        r1 = sort(root1)
        r2 = sort(root2)
        
        result = []
        p1 = 0
        p2 = 0
        while p1 < len(r1) and p2 < len(r2):
            if r1[p1] <= r2[p2]:
                result.append(r1[p1])
                p1 += 1
            else:
                result.append(r2[p2])
                p2 += 1
        
        while p1 < len(r1):
            result.append(r1[p1])
            p1 += 1
        
        while p2 < len(r2):
            result.append(r2[p2])
            p2 += 1
            
        return result
            
            
                
            