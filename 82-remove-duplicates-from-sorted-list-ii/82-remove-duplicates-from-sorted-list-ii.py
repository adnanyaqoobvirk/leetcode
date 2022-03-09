# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        while prev.next and prev.next.next:
            curr = prev.next.next
            if curr.val == prev.next.val:
                while curr and curr.val == prev.next.val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
        return dummy.next