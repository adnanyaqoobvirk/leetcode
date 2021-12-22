# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes, curr = [], head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        lo, hi = 0, len(nodes) - 1
        while lo < hi:
            nodes[lo].next = nodes[hi]
            nodes[hi].next = nodes[lo + 1] if lo + 1 <= hi - 1 else None
            lo += 1
            hi -= 1
        nodes[lo].next = None
        return head