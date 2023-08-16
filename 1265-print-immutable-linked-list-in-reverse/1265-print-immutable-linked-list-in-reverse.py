# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode', tail: 'ImmutableListNode' = None) -> None:
        if not head:
            return 
        
        if head == tail:
            head.printValue()
            return
            
        slow = fast = head
        while fast and fast.getNext() and fast != tail and fast.getNext() != tail:
            slow = slow.getNext()
            fast = fast.getNext().getNext()

        self.printLinkedListInReverse(slow.getNext(), tail)
        self.printLinkedListInReverse(head, slow)