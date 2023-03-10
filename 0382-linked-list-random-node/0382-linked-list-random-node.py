# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        curr = self.head
        val = curr.val
        i = 1
        while curr:
            j = randint(1, i)
            if j <= 1:
                val = curr.val
            curr = curr.next
            i += 1
        return val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()