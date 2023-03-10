# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.size = 0
        curr = head
        while curr:
            self.size += 1
            curr = curr.next

    def getRandom(self) -> int:
        curr = self.head
        for _ in range(randint(0, self.size - 1)):
            curr = curr.next
        return curr.val
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()