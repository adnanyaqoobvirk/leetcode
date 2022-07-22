# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lcurr = lhead = ListNode()
        gcurr = ghead = ListNode()
        
        curr = head
        while curr:
            ncurr = curr.next
            curr.next = None
            
            if curr.val < x:
                lcurr.next = curr
                lcurr = lcurr.next
            else:
                gcurr.next = curr
                gcurr = gcurr.next
            
            curr = ncurr
            
        lcurr.next = ghead.next
        
        return lhead.next