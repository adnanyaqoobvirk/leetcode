# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans, stack, curr, i = [], [] , head, 0
        while curr:
            while stack and stack[-1][0] < curr.val:
                ans[stack.pop()[1]] = curr.val
                
            stack.append((curr.val, i))
            ans.append(0)
            
            i += 1
            curr = curr.next
        return ans