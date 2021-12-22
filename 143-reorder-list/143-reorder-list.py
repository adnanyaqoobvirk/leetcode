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
        
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        left, right = head, prev
        while right.next:
            left.next, left = right, left.next
            right.next, right = left, right.next