# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        def helper(curr: Optional[ListNode]) -> Optional[ListNode]:
            if not curr.next:
                nonlocal nhead
                nhead = curr
                return curr

            helper(curr.next).next = curr
            curr.next = None
            return curr
        
        nhead = None
        helper(head)
        return nhead