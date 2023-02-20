class MyHashMap:

    def __init__(self, capacity = 64, load_factor = 0.8):
        self.lf = load_factor
        self.cap = capacity
        self.data = [[] for _ in range(self.cap)]
        self.size = 0

    def _resize(self, size):
        self.cap = size
        data = [[] for _ in range(self.cap)]
        for l in self.data:
            for k, v in l:
                data[k % self.cap].append([k, v])
        self.data = data
        
    def put(self, key: int, value: int) -> None:
        if self.size / self.cap > self.lf:
            self._resize(self.cap * 2)
            
        l = self.data[key % self.cap]
        for kv in l:
            if kv[0] == key:
                kv[1] = value
                break
        else:
            l.append([key, value])
            self.size += 1
        
    def get(self, key: int) -> int:
        for kv in self.data[key % self.cap]:
            if kv[0] == key:
                return kv[1]
        return -1
    
    def remove(self, key: int) -> None:
        if self.size / self.lf < self.lf / 2:
            self._resize(self.cap // 2)
        
        l = self.data[key % self.cap]
        for i in range(len(l)):
            if l[i][0] == key:
                l.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)