class MovingAverage:

    def __init__(self, size: int):
        self.q, self.total, self.pos = [inf] * size, 0, 0
        
    def next(self, val: int) -> float:
        if self.q[self.pos] != inf:
            self.total -= self.q[self.pos]
        
        self.q[self.pos] = val
        self.total += val
        
        self.pos = (self.pos + 1) % len(self.q)
        
        return self.total / (len(self.q) if self.q[self.pos] != inf else self.pos)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)