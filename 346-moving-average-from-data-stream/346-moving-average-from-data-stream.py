class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)
        self.total += val
        if len(self.window) > self.size:
            self.total -= self.window.popleft()
        return self.total / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)