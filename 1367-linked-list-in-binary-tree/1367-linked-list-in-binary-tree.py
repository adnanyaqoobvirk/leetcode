# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(t: TreeNode, l: ListNode) -> bool:
            if not l:
                return True
            
            if not t:
                return False
            
            if t.val != l.val:
                return False
            
            return match(t.left, l.next) or match(t.right, l.next)
        
        def helper(curr: TreeNode) -> bool:
            if not curr:
                return False
            
            if curr.val == head.val and match(curr, head):
                return True
            
            return helper(curr.left) or helper(curr.right)
        return helper(root)