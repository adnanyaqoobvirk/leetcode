# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, curr = [], l1
        while curr:
            s1.append(curr.val)
            curr = curr.next
        
        s2, curr = [], l2
        while curr:
            s2.append(curr.val)
            curr = curr.next
    
        s, c = [], 0
        while s1 and s2:
            c, d = divmod(s1.pop() + s2.pop() + c, 10)
            s.append(d)
        
        s3 = s1 if s1 else s2
        while s3:
            c, d = divmod(s3.pop() + c, 10)
            s.append(d)
        
        curr = l = ListNode(s.pop() if c == 0 else c)
        while s:
            curr.next = ListNode(s.pop())
            curr = curr.next
            
        return l