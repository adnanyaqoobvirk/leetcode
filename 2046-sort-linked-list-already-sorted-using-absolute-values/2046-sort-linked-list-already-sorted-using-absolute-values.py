# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead = head
        prev, curr = None, head
        while curr:
            if curr.val < 0 and prev:
                prev.next, curr.next = curr.next, nhead
                nhead, curr = curr, prev.next
            else:
                prev, curr = curr, curr.next
        return nhead