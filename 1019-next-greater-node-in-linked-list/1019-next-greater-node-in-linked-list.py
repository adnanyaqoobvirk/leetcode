# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        stack = []
        ans = [0] * len(values)
        for i in reversed(range(len(values))):
            while stack and stack[-1] <= values[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            stack.append(values[i])
        return ans