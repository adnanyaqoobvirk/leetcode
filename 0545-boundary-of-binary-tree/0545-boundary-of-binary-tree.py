# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ans = [root.val]
        
        curr = root.left
        while curr:
            if curr.left or curr.right:
                ans.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
            
        stack = []
        if root.right:
            stack.append(root.right)
            
        if root.left:
            stack.append(root.left)
            
        while stack:
            curr = stack.pop()
            
            if not curr.left and not curr.right:
                ans.append(curr.val)
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        
        curr = root.right
        right_boundry = []
        while curr:
            if curr.left or curr.right:
                right_boundry.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
            
        while right_boundry:
            ans.append(right_boundry.pop())
        
        return ans
        