class Node:
    def __init__(self, val: int = -1, key: int = -1, next: 'Node' = None):
        self.key = key
        self.val = val
        self.next = next
        
class MyHashMap:

    def __init__(self):
        self.keys = [None] * 31
        self.size = 0
        
    def _loadfactor(self) -> float:
        return self.size / len(self.keys)
    
    def _hash(self, key: int) -> int:
        return (17167 * key) % len(self.keys)
    
    def _resize(self):
        keys = self.keys
        self.keys = [None] * (len(self.keys) * 3)
        for key in keys:
            while key:
                h = self._hash(key.key)
                head = self.keys[h]
                if not head:
                    self.keys[h] = Node(key.val, key.key)
                else:
                    curr = head
                    while curr.next:
                        curr = curr.next
                    curr.next = Node(key.val, key.key)
                key = key.next
        
    def put(self, key: int, value: int) -> None:
        if self._loadfactor() >= 0.8:
            self._resize()
            
        h = self._hash(key)
        head = self.keys[h]
        if not head:
            self.keys[h] = Node(value, key)
        else:
            prev, curr = None, head
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev, curr = curr, curr.next
            prev.next = Node(value, key)
        self.size += 1

    def get(self, key: int) -> int:
        h = self._hash(key)
        head = self.keys[h]
        while head and head.key != key:
            head = head.next
        return head.val if head else -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        head = self.keys[h]
        if head:
            if head.key == key:
                self.keys[h] = head.next
                self.size -= 1
            else:
                prev, curr = head, head.next
                while curr:
                    if curr.key == key:
                        prev.next = curr.next
                        self.size -= 1
                        break
                    prev, curr = curr, curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)