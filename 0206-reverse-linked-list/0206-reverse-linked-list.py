# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        def helper(curr: ListNode) -> ListNode:
            if not curr.next:
                return curr
            
            nhead = helper(curr.next)
            curr.next.next = curr
            curr.next = None
            
            return nhead
        
        return helper(head)