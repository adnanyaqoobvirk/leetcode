class MovingAverage:

    def __init__(self, size: int):
        self.q  = [0] * size
        self.total = self.pos = self.count = 0
        
    def next(self, val: int) -> float:
        self.total += val - self.q[self.pos]
        self.q[self.pos] = val
        self.pos = (self.pos + 1) % len(self.q)
        self.count += 1
        
        return self.total / min(self.count, len(self.q))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)