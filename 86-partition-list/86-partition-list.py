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
            if curr.val < x:
                lcurr.next = ListNode(curr.val)
                lcurr = lcurr.next
            else:
                gcurr.next = ListNode(curr.val)
                gcurr = gcurr.next
            curr = curr.next
            
        lcurr.next = ghead.next
        
        return lhead.next