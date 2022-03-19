from sortedcontainers import SortedSet

class FreqStack:

    def __init__(self):
        self.ss = SortedSet()
        self.map = {}
        self.count = 0

    def push(self, val: int) -> None:
        self.count += 1
        if val in self.map:
            freq = self.map[val]
            self.ss.add((freq + 1, self.count, val))
            self.map[val] = freq + 1
        else:
            self.map[val] = 1
            self.ss.add((1, self.count, val))

    def pop(self) -> int:
        freq, count, val = self.ss.pop()
        if freq == 1:
            del self.map[val]
        else:
            self.map[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()