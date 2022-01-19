# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr: Optional[ListNode]) -> Optional[ListNode]:
            if not curr:
                return None

            if not curr.next:
                nonlocal nhead
                nhead = curr
                return curr

            node = helper(curr.next)
            node.next, curr.next = curr, None
            return curr
    
        nhead = None
        curr = helper(head)
        return nhead