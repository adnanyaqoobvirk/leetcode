class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.items = {}

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        
        value = self.items[key]
        del self.items[key]
        self.items[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            del self.items[key]
        self.items[key] = value

        if len(self.items) > self.cap:
            k = next(iter(self.items.keys()))
            del self.items[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)