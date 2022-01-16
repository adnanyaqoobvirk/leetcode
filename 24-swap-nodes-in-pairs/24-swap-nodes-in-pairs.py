# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        nhead = curr = head.next
        p2, p1 = None, head
        while p1 and curr:
            p1.next, curr.next = curr.next, p1
            if p2: p2.next = curr
            p2, p1 = p1, p1.next
            curr = p1.next if p1 else None
        return nhead