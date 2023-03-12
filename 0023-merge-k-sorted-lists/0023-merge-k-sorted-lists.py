# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i, head in enumerate(lists):
            if head:
                h.append((head.val, i, head))
        heapify(h)
        
        dummy = curr = ListNode()
        while h:
            curr.next = heappop(h)[2]
            curr = curr.next
            if curr.next:
                i += 1
                heappush(h, (curr.next.val, i, curr.next))
        return dummy.next