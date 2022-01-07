from random import sample

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        r = self.head.val
        curr, cnt = self.head.next, 2
        while curr:
            if randint(1, cnt) == 1:
                r = curr.val
            cnt += 1
            curr = curr.next
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()