# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size, curr = 0, head
        while curr:
            curr = curr.next
            size += 1
        
        q, r = divmod(size, k)
        
        res, curr = [], head
        
        for _ in range(r):
            res.append(curr)
            prev = curr
            for _ in range(q + 1):
                prev, curr = curr, curr.next
            prev.next = None
        
        for _ in range(r, k):
            res.append(curr)
            if curr:
                prev = curr
                for _ in range(q):
                    prev, curr = curr, curr.next
                prev.next = None
        
        return res
        
        
        