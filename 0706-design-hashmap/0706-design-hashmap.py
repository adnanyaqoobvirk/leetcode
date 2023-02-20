class Node:
    def __init__(self, key = -1, val = -1, nxt = None):
        self.key, self.val, self.nxt = key, val, nxt
        
class MyHashMap:

    def __init__(self, capacity = 61, load_factor = 0.7):
        self.lf = load_factor
        self.cap = capacity
        self.data = [Node() for _ in range(self.cap)]
        self.size = 0

    def _resize(self, size):
        self.cap = size
        data = [Node() for _ in range(self.cap)]
        for head in self.data:
            curr = head.nxt
            while curr:
                nhead = data[curr.key % self.cap]
                nhead.nxt = Node(curr.key, curr.val, nhead.nxt)
                curr = curr.nxt
        self.data = data
        
    def put(self, key: int, value: int) -> None:
        if self.size / self.cap > self.lf:
            self._resize(self.cap * 2)
            
        head = self.data[key % self.cap]
        curr = head.nxt
        while curr:
            if curr.key == key:
                curr.val = value
                break
            curr = curr.nxt
        else:
            head.nxt = Node(key, value, head.nxt)
            self.size += 1
        
    def get(self, key: int) -> int:
        curr = self.data[key % self.cap].nxt
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.nxt
        return -1
    
    def remove(self, key: int) -> None:
        if self.size / self.lf < self.lf / 4:
            self._resize(self.cap // 2)
        
        curr = self.data[key % self.cap]
        while curr.nxt:
            if curr.nxt.key == key:
                nxt = curr.nxt
                curr.nxt = nxt.nxt
                nxt.nxt = None
                self.size -= 1
                break
            curr = curr.nxt

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)