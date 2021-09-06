class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = [None] * size
        self.count = self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        i = self.count % self.size
        self.total += val
        if self.count >= self.size:
            self.total -= self.window[i]
        self.count += 1
        self.window[i] = val
        return self.total / min(self.count, self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)