# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, slow, fast = None, head, head.next
        while fast and fast.next:
            prev, slow.next, slow = slow, prev, slow.next
            fast = fast.next.next
        second, slow.next = slow.next, prev
        
        if not fast:
            slow = slow.next
        
        while slow:
            if slow.val != second.val:
                return False
            slow = slow.next
            second = second.next
        return True
        
            