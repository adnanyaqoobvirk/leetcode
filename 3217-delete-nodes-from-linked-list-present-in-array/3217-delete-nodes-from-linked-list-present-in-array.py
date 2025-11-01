# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        toRemove = set(nums)
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            if curr.val in toRemove:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev, curr = curr, curr.next
        return dummy.next