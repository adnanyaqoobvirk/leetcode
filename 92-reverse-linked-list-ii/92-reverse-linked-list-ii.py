# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head or not head.next:
            return head
        
        sentinal = ListNode(0, head)
        
        ltail = sentinal
        for i in range(left - 1):
            ltail = ltail.next
        
        prev, curr = ltail.next, ltail.next.next
        for _ in range(right - left):
            ncurr, curr.next = curr.next, prev
            prev, curr = curr, ncurr
        ltail.next.next = curr
        ltail.next = prev
        
        return sentinal.next