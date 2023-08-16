# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(root: ListNode):
            prev, curr = root, root.next
            prev.next = None
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        head = reverse(head)
        
        curr, carry = head, 1
        while curr and carry:
            carry, curr.val = divmod(curr.val + carry, 10)
            prev, curr = curr, curr.next
            
        if carry:
            prev.next = ListNode(carry)
            
        return reverse(head)
        