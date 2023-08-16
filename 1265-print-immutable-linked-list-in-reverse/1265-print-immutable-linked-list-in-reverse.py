# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        size, curr = 0, head
        while curr:
            size, curr = size + 1, curr.next
        
        bsize, buckets, curr, count = int(math.sqrt(size)), [], head, 0
        for i in range(size):
            if i % bsize == 0:
                buckets.append(curr)
            curr = curr.next
        
        for curr in reversed(buckets):
            stack = []
            for _ in range(bsize):
                if not curr:
                    break
                stack.append(curr)
                curr = curr.next
            
            for curr in reversed(stack):
                curr.printValue()