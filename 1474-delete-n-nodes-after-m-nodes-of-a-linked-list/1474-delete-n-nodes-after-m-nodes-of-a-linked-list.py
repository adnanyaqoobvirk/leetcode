# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head
        mptr = None
        while current:
            mcount = 1
            while mcount < m and current:
                current = current.next
                mcount += 1
            
            if current:
                mptr = current
                ncount = 0
                while ncount <= n and current:
                    current = current.next
                    ncount += 1
                mptr.next = current
        return head
            