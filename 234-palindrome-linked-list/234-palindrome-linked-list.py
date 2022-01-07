# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        
        prev, curr = None, head
        while curr != slow:
            prev, curr.next, curr = curr, prev, curr.next
        curr.next = prev
        
        if not fast:
            curr = curr.next
        
        while curr:
            if curr.val != second.val:
                return False
            curr = curr.next
            second = second.next
        return True
        
            