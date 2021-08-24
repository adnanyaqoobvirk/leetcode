class MRUQueue:

    def __init__(self, n: int):
        self.csize = int(math.sqrt(n))
        self.chunks = []
        for i in range(0, n):
            if i % self.csize == 0:
                self.chunks.append(deque())
            self.chunks[-1].append(i + 1)
            
    def fetch(self, k: int) -> int:
        i = (k - 1) // self.csize
        
        e = self.chunks[i][(k - 1) % self.csize]
        self.chunks[i].remove(e)
        for j in range(i + 1, len(self.chunks)):
            self.chunks[j - 1].append(self.chunks[j].popleft())
        self.chunks[-1].append(e)
        
        return e

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)