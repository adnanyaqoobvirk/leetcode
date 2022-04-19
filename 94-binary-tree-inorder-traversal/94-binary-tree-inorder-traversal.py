# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, ans = root, []
        while curr:
            if curr.left:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
                if not node.right:
                    node.right, curr = curr, curr.left
                else:
                    node.right = None
                    ans.append(curr.val)
                    curr = curr.right
            else:
                ans.append(curr.val)
                curr = curr.right
        return ans