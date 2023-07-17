# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur: ListNode):
            pre = None
            while cur:
                nxt, cur.next = cur.next, pre
                pre, cur = cur, nxt
            return pre
        
        l = s = ListNode()
        cur1, cur2, c = reverse(l1), reverse(l2), 0
        while cur1 and cur2:
            c, d = divmod(cur1.val + cur2.val + c, 10)
            l.next = ListNode(d)
            l, cur1, cur2 = l.next, cur1.next, cur2.next
        
        cur = cur1 if cur1 else cur2
        while cur:
            c, d = divmod(cur.val + c, 10)
            l.next = ListNode(d)
            l, cur = l.next, cur.next
        
        if c > 0:
            l.next = ListNode(c)
        
        return reverse(s.next)