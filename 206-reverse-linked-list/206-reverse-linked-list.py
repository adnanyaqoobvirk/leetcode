# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr: Optional[ListNode]) -> Optional[ListNode]:
            if curr:
                if not curr.next:
                    nonlocal nhead
                    nhead = curr
                else:
                    helper(curr.next).next = curr
                curr.next = None
                return curr
        nhead = None
        helper(head)
        return nhead