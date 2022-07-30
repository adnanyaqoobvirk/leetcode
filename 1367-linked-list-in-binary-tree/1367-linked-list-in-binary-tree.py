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
        @cache
        def helper(lcurr: ListNode, tcurr: TreeNode) -> bool:
            if not lcurr:
                return True
            
            if not tcurr:
                return False
            
            ans = False
            if tcurr.val == lcurr.val:
                ans = helper(lcurr.next, tcurr.left) or helper(lcurr.next, tcurr.right)
            
            return ans or helper(head, tcurr.left) or helper(head, tcurr.right)
        return helper(head, root)