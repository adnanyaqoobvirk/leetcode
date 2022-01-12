# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, curr, ans = [], root, []
        while curr or stack:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if stack and node.right == stack[-1]:
                    curr = stack.pop()
                    stack.append(node)
                else:
                    ans.append(node.val)
        return ans