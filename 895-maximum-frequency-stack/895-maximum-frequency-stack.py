class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)
        self.maxfreq = max(self.freq[val], self.maxfreq)

    def pop(self) -> int:
        val = self.stacks[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.stacks[self.maxfreq]:
            self.maxfreq -= 1
        return val
    
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()