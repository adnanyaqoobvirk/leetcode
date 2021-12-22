# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr, slow.next = slow, slow.next, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        left, right = head, prev
        while left and right:
            lnode, rnode = left.next, right.next
            left.next = right
            right.next = lnode if lnode and rnode else None
            left, right = lnode, rnode