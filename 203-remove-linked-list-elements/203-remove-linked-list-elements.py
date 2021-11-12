# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinal = dst_curr = ListNode()
        src_curr = head
        while src_curr:
            if src_curr.val != val:
                dst_curr.next = ListNode(src_curr.val)
                dst_curr = dst_curr.next
            src_curr = src_curr.next
        return sentinal.next