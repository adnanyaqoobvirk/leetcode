# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr, count = head, k - 1
        while curr and count > 0:
            curr = curr.next
            count -= 1
        
        kstart = curr
        curr, kcurr = head, curr
        while kcurr.next:
            kcurr = kcurr.next
            curr = curr.next
        
        kstart.val, curr.val = curr.val, kstart.val
        return head