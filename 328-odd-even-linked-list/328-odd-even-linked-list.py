# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        even_head = even_curr = head.next
        odd_curr, curr, even = head, head.next.next, False
        while curr:
            if even:
                even_curr.next, even_curr = curr, curr
            else:
                odd_curr.next, odd_curr = curr, curr
            even, curr = not even, curr.next
        
        odd_curr.next, even_curr.next = even_head, None
        return head