class MaxStack:

    def __init__(self):
        self.stack = []
        self.max, self.maxi = float('-inf'), None
        
    def setMax(self) -> None:
        self.max, self.maxi = float('-inf'), None
        for i in reversed(range(len(self.stack))):
            if self.stack[i] > self.max:
                self.max, self.maxi = self.stack[i], i

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x >= self.max:
            self.max, self.maxi = x, len(self.stack) - 1

    def pop(self) -> int:
        v = self.stack.pop()
        if v == self.max:
            self.setMax()
        return v

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        v = self.stack.pop(self.maxi)
        self.setMax()
        return v


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()