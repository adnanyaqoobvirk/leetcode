class FreqStack:

    def __init__(self):
        self.h = []
        self.time = 0
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.time += 1
        self.freq[val] += 1
        heappush(self.h, (-self.freq[val], -self.time, val))

    def pop(self) -> int:
        _, _, val = heappop(self.h)
        self.freq[val] -= 1
        return val
    
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()