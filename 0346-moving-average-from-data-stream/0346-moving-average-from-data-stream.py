class MovingAverage:

    def __init__(self, size: int):
        self.q, self.total, self.size = deque(), 0, size
        
    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val
        
        if len(self.q) > self.size:
            self.total -= self.q.popleft()
        
        return self.total / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)