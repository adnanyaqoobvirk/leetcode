# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA, currA = 0, headA
        while currA:
            currA = currA.next
            sizeA += 1
        
        sizeB, currB = 0, headB
        while currB:
            currB = currB.next
            sizeB += 1
        
        if sizeA > sizeB:
            headA, headB = headB, headA
            
        currB = headB
        for _ in range(abs(sizeB - sizeA)):
            currB = currB.next
        
        currA = headA
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None
        