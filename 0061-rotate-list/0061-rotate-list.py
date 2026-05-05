# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        fast = head
        i = 0
        while i < k:
            if not fast:
                break
            fast = fast.next
            i += 1

        if not fast:
            fast = head
            k = k % i
            for _ in range(k):
                fast = fast.next
        
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        if not slow.next:
            return head

        nhead = slow.next
        slow.next = None
        fast.next = head

        return nhead