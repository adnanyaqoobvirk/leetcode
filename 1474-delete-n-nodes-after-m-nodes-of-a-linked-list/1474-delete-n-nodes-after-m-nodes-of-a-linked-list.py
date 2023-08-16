# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        i = j = 0
        curr = prev = head
        while curr:
            if i == m:
                if j < n:
                    j += 1
                    curr = curr.next
                    continue
                else:
                    prev.next = curr
                    i = j = 0
            i += 1
            prev, curr = curr, curr.next
        prev.next = None
        return head