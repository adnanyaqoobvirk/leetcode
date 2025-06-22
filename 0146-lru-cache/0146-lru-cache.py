class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class DList:
    def __init__(self):
        self.head = self.tail = None
    
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return node
    
    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node
    
    def delete(self, curr):
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.items = {}
        self.ll = DList()

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1

        node = self.items[key]
        self.ll.delete(node)
        self.items[key] = self.ll.prepend(node.data)
        return node.data[1]

    def put(self, key: int, value: int) -> None:
        if key not in self.items:
            self.items[key] = self.ll.prepend((key, value))
        else:
            node = self.items[key]
            self.ll.delete(node)
            self.items[key] = self.ll.prepend((key, value))
        
        if len(self.items) > self.cap:
            del self.items[self.ll.tail.data[0]]
            self.ll.delete(self.ll.tail)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)