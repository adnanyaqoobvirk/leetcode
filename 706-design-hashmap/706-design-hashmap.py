class MyHashMap:

    def __init__(self):
        self.keys = [[] for _ in range(2069)]
        self.size = 0
        
    def _loadfactor(self) -> float:
        return self.size / len(self.keys)
    
    def _hash(self, key: int) -> int:
        return (17167 * key) % len(self.keys)
    
    def _resize(self):
        keys = self.keys
        self.keys = [[] * (len(self.keys) * 3)]
        for kl in keys:
            for k, v in kl:
                self.keys[self._hash(k)].append((k, v))
        
    def put(self, key: int, value: int) -> None:
        # if self._loadfactor() >= 0.8:
        #     self._resize()
            
        h = self._hash(key)
        for i, (k, v) in enumerate(self.keys[h]):
            if k == key:
                self.keys[h][i] = (key, value) 
                break
        else:
            self.keys[h].append((key, value))
            self.size += 1

    def get(self, key: int) -> int:
        h = self._hash(key)
        for k, v in self.keys[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        for i, (k, v) in enumerate(self.keys[h]):
            if k == key:
                del self.keys[h][i]
                self.size -= 1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)