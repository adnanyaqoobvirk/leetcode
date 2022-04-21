class MyHashSet:

    def __init__(self):
        self.keys = [[] for _ in range(32)]
        self.size = 0

    def add(self, key: int) -> None:
        if self.size / len(self.keys) > 0.8:
            keys = [[] for _ in range(len(self.keys)*2)]
            for kl in self.keys:
                for k in kl:
                    keys[k % len(keys)].append(k)
            self.keys = keys
        for k in self.keys[key % len(self.keys)]:
            if k == key:
                break
        else:  
            self.keys[key % len(self.keys)].append(key)
            self.size += 1
        
    def remove(self, key: int) -> None:
        try:
            self.keys[key % len(self.keys)].remove(key)
            self.size -= 1
        except:
            pass

    def contains(self, key: int) -> bool:
        for k in self.keys[key % len(self.keys)]:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)