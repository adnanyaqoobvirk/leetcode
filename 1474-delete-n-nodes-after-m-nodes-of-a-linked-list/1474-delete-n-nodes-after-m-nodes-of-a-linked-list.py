# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinal = curr = ListNode()
        i = j = 0
        while head:
            if i == m:
                if j < n:
                    j += 1
                    head = head.next
                    continue
                else:
                    i = j = 0
            i += 1
            curr.next = ListNode(head.val)
            curr, head = curr.next, head.next
        return sentinal.next