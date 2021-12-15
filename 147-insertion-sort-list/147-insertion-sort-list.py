# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinal, ocurr, head.next = ListNode(next=head), head.next, None
        while ocurr:
            iprev, icurr = sentinal, sentinal.next
            while icurr and icurr.val < ocurr.val:
                iprev, icurr = icurr, icurr.next
            iprev.next, ocurr = ocurr, ocurr.next
            iprev.next.next = icurr
        return sentinal.next