class Node:
    def __init__(self, val = -1, nxt = None):
        self.val = val
        self.next = nxt
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def getNode(self, index: int) -> int:
        curr = self.head
        for _ in range(index + 1):
            if not curr:
                return None
            
            curr = curr.next
        return curr
    
    def get(self, index: int) -> int:
        curr = self.getNode(index)
        return -1 if not curr else curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.size:
            curr = self.getNode(index - 1)
            curr.next = Node(val, curr.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            curr = self.getNode(index - 1)
            curr.next = curr.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)