# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        bsize = int(math.sqrt(size))
        buckets = [head]
        curr = head
        count = 0
        while curr:
            if count < bsize:
                count += 1
            else:
                count = 1
                buckets.append(curr)
            curr = curr.next
        
        for curr in reversed(buckets):
            stack = []
            for _ in range(bsize):
                if not curr:
                    break
                stack.append(curr)
                curr = curr.next
            
            for n in reversed(stack):
                n.printValue()
            