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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(lo, hi):
            nonlocal curr
            
            if lo > hi:
                return None
            
            mid = lo + hi >> 1
            
            left = helper(lo, mid - 1)
            
            root = TreeNode(curr.val, left)
            curr = curr.next
            
            root.right = helper(mid + 1, hi)
            
            return root
        
        size, curr = 0, head
        while curr:
            size += 1
            curr = curr.next
            
        curr = head
        return helper(0, size - 1)