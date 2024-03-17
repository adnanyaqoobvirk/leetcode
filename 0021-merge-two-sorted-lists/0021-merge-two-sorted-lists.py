# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = t = ListNode()
        l1 = list1
        l2 = list2
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            
            t = t.next
        
        if l1 is not None:
            t.next = l1
        else:
            t.next = l2
        
        return dummy.next
        