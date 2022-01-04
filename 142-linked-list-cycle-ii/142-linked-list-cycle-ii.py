# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        
        if slow != fast:
            return None
        
        p1, p2 = head, slow.next
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1