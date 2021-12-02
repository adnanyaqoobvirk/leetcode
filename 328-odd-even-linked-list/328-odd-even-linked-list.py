# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr_even = even_head = head.next
        curr, curr_odd, even = head.next.next, head, False
        while curr:
            if even:
                curr_even.next = curr
                curr_even = curr_even.next
            else:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            even = not even
            curr = curr.next
        curr_odd.next, curr_even.next = even_head, None
        return head