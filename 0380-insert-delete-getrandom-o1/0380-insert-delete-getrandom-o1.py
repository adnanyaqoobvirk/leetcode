from random import randint

class RandomizedSet:

    def __init__(self):
        self.vlist = []
        self.vmap = {}

    def insert(self, val: int) -> bool:
        if val in self.vmap:
            return False
        
        self.vlist.append(val)
        self.vmap[val] = len(self.vlist) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vmap:
            return False
        
        self.vlist[self.vmap[val]], self.vmap[self.vlist[-1]] = self.vlist[-1], self.vmap[val]
        self.vlist.pop()
        del self.vmap[val]
        return True

    def getRandom(self) -> int:
        return self.vlist[randint(0, len(self.vlist) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()