class RecentCounter:

    def __init__(self):
        self.stack = []
        self.pos = 0
        
    def ping(self, t: int) -> int:
        self.stack.append(t)
        while self.stack[self.pos] < t - 3000:
            self.pos += 1
        return len(self.stack) - self.pos


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)