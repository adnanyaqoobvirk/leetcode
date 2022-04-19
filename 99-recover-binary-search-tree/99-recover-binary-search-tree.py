# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes, stack, head = [], [], root
        while head or stack:
            if head:
                stack.append(head)
                head = head.left
            else:
                curr = stack.pop()
                nodes.append(curr)
                if curr.right:
                    head = curr.right
        
        left, right, n = 0, 1, len(nodes)
        while right < n and nodes[left].val < nodes[right].val:
            left += 1
            right += 1
        
        while right < n and nodes[left].val > nodes[right].val:
            right += 1
            
        nodes[left].val, nodes[right - 1].val = nodes[right - 1].val, nodes[left].val