class Node:
    def __init__(self, val: int = 0, prev: 'Node' = None, next: 'Node' = None) -> None:
        self.val, self.prev, self.next = val, prev, next
        
class MyLinkedList:

    def __init__(self):
        self.fdummy = Node()
        self.bdummy = Node(prev=self.fdummy)
        self.fdummy.next = self.bdummy
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if index > (self.size // 2):
            curr = self.bdummy
            while index < self.size:
                curr = curr.prev
                index += 1
            return curr.val
        else:
            curr = self.fdummy
            while index >= 0:
                curr = curr.next
                index -= 1
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        self.fdummy.next.prev = Node(val, self.fdummy, self.fdummy.next)
        self.fdummy.next = self.fdummy.next.prev
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.bdummy.prev.next = Node(val, self.bdummy.prev, self.bdummy)
        self.bdummy.prev = self.bdummy.prev.next
        self.size += 1
        
    def getNodeAtIndex(self, index: int) -> Node:
        if index < 0 or index >= self.size:
            return
        
        if index > (self.size // 2):
            curr = self.bdummy
            while index < self.size:
                curr = curr.prev
                index += 1
        else:
            curr = self.fdummy
            while index >= 0:
                curr = curr.next
                index -= 1
        return curr

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        curr = self.getNodeAtIndex(index)
        if curr:
            curr.prev.next = Node(val, curr.prev, curr)
            curr.prev = curr.prev.next
            self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        curr = self.getNodeAtIndex(index)
        if curr:
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            self.size -= 1
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)