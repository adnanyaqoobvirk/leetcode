# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinal, carry = ListNode(), 0
        curr, curr1, curr2 = sentinal, l1, l2
        while curr1 and curr2:
            carry, d = divmod(curr1.val + curr2.val + carry, 10)
            curr.next = ListNode(d)
            curr, curr1, curr2 = curr.next, curr1.next, curr2.next
        
        l = curr1 if curr1 else curr2
        while l:
            carry, d = divmod(l.val + carry, 10)
            curr.next = ListNode(d)
            curr, l = curr.next, l.next
        
        if carry:
            curr.next = ListNode(carry)
            
        return sentinal.next