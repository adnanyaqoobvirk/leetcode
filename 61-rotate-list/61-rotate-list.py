# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        vals, curr = [], head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        ops = k % len(vals)
        if not ops:
            return head
        
        curr = head
        for i in range(-ops, 0, 1):
            curr.val = vals[i]
            curr = curr.next
        
        for i in range(len(vals) - ops):
            curr.val = vals[i]
            curr = curr.next
        
        return head