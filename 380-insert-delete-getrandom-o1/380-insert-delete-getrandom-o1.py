from random import randint

class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.elements = []
        
    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.elements.append(val)
        self.indices[val] = len(self.elements) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        curri = self.indices[val]
        self.elements[-1], self.elements[curri] = self.elements[curri], self.elements[-1]
        self.indices[self.elements[curri]] = curri
        
        self.elements.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return self.elements[randint(0, len(self.elements) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()