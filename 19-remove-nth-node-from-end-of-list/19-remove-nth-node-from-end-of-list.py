# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for _ in range(n):
            curr = curr.next
        
        sentinal = ListNode(0, head)
        p2, p1 = sentinal, head
        while curr:
            curr = curr.next
            p2, p1 = p1, p1.next
        
        p2.next = p1.next
        return sentinal.next