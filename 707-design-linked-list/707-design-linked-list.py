class Node:
    def __init__(self, val: int = 0, nxt: 'Node' = None) -> None:
        self.val, self.next = val, nxt
    
class MyLinkedList:

    def __init__(self):
        self.sentinal, self.size = Node(), 0

    def get(self, index: int) -> int:
        if 0 > index or index >= self.size:
            return -1
        
        curr, i = self.sentinal.next, 0
        while curr and i < index:
            curr = curr.next
            i += 1
            
        return -1 if not curr else curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if 0 > index or index > self.size:
            return
        
        prev, curr, i = self.sentinal, self.sentinal.next, 0
        while curr and i < index:
            prev, curr = curr, curr.next
            i += 1
        
        if not curr:
            prev.next = Node(val)
        else:
            prev.next = Node(val, curr)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 > index or index >= self.size:
            return
        
        prev, curr, i = self.sentinal, self.sentinal.next, 0
        while curr and i < index:
            prev, curr = curr, curr.next
            i += 1
        
        prev.next, curr.next = curr.next, None
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)