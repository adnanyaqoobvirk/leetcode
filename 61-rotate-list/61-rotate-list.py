# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        size, tail, curr = 0, None, head
        while curr:
            size += 1
            tail, curr = curr, curr.next
            
        ops = k % size
        if not ops:
            return head
    
        curr = head
        for i in range(size - ops - 1):
            curr = curr.next
        nhead, tail.next, curr.next = curr.next, head, None 
        
        return nhead