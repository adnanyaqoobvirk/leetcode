# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        lsize, prev, curr = 0, None, head
        while curr:
            lsize, prev, curr = lsize + 1, curr, curr.next
            
        k %= lsize
        if k == 0:
            return head
        
        curr = head
        for _ in range(lsize - k - 1):
            curr = curr.next
        
        nhead, prev.next, curr.next = curr.next, head, None
        return nhead
            