# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l2_tail = list2
        while l2_tail.next:
            l2_tail = l2_tail.next
        
        l1_prev = list1
        l1_curr = list1.next
        count = 1
        while count != a:
            l1_prev, l1_curr = l1_curr, l1_curr.next
            count += 1
        
        l1_prev.next = list2
        while count != b:
            l1_curr = l1_curr.next
            count += 1
        l2_tail.next = l1_curr.next
        
        return list1