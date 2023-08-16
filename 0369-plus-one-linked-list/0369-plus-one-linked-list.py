# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next
            
        carry = 1
        while stack and carry:
            node = stack.pop()
            carry, node.val = divmod(node.val + carry, 10)
        
        if carry:
            head = ListNode(1, head)
        
        return head
            