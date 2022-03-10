# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = curr = ListNode()
        p1, p2, carry = l1, l2, 0
        while p1 and p2:
            carry, digit = divmod(p1.val + p2.val + carry, 10)
            curr.next = ListNode(digit)
            p1, p2, curr = p1.next, p2.next, curr.next
        
        p = p1 if p1 else p2
        while p:
            carry, digit = divmod(p.val + carry, 10)
            curr.next = ListNode(digit)
            p, curr = p.next, curr.next
        
        if carry:
            curr.next = ListNode(carry)
            
        return dummy.next