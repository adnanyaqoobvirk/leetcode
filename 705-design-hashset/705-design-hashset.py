class Node:
    def __init__(self, val: int = -1, next: 'Node' = None):
        self.val = val
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.keys = [None] * 32
        self.size = 0

    def resize(self):
        keys = [None] * (len(self.keys) * 2)
        for key in self.keys:
            while key:
                h = key.val % len(keys)
                head = keys[h]
                if not head:
                    keys[h] = Node(key.val)
                else:
                    curr = head
                    while curr.next:
                        curr = curr.next
                    curr.next = Node(key.val)
                key = key.next
        self.keys = keys
    
    def add(self, key: int) -> None:
        if self.size / len(self.keys) >= 0.8:
            self.resize()
            
        h = key % len(self.keys)
        head = self.keys[h]
        if not head:
            self.keys[h] = Node(key)
        else:
            prev, curr = None, head
            while curr:
                if curr.val == key:
                    return
                prev, curr = curr, curr.next
            prev.next = Node(key)
        self.size += 1
            
    def remove(self, key: int) -> None:
        h = key % len(self.keys)
        head = self.keys[h]
        if head:
            if head.val == key:
                self.keys[h] = head.next
                self.size -= 1
            else:
                prev, curr = head, head.next
                while curr:
                    if curr.val == key:
                        prev.next = curr.next
                        self.size -= 1
                        break
                    prev, curr = curr, curr.next

    def contains(self, key: int) -> bool:
        h = key % len(self.keys)
        head = self.keys[h]
        while head and head.val != key:
            head = head.next
        return head != None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)