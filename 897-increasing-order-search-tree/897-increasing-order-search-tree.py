# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(curr: TreeNode) -> Tuple[TreeNode, TreeNode]:
            if not curr:
                return (None, None)
            
            left_head, left_tail = helper(curr.left)
            right_head, right_tail = helper(curr.right)
            
            if not left_head:
                left_head = left_tail = curr
            else:
                left_tail.right = curr
                left_tail = curr
            left_tail.left = None
            
            if not right_head:
                right_tail = left_tail
            else:
                left_tail.right = right_head
            return left_head, right_tail
        head, tail = helper(root)
        return head