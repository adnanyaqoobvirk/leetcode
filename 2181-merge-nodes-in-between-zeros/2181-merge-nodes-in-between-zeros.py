# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero = curr = head.next
        curr_sum = 0
        while curr:
            if curr.val == 0:
                zero.val = curr_sum
                curr_sum = 0
                zero.next = curr.next
                zero = zero.next
            else:
                curr_sum += curr.val
            curr = curr.next
        return head.next