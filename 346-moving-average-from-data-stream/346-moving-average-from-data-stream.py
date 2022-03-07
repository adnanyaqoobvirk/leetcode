class MovingAverage:

    def __init__(self, size: int):
        self.q = [0] * size
        self.total = self.size = self.tail = 0

    def next(self, val: int) -> float:
        if self.size == len(self.q):
            self.total -= self.q[self.tail]
        else:
            self.size += 1
            
        self.q[self.tail] = val
        self.total += val
        self.tail = (self.tail + 1) % len(self.q)
        return self.total / self.size
    
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)