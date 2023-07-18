class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        v = self.d[key]
        del self.d[key]
        self.d[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            
        self.d[key] = value
        
        if len(self.d) > self.c:
            del self.d[next(iter(self.d))]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)