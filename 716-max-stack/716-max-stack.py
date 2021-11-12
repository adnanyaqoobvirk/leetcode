class MaxStack:

    def __init__(self):
        self.stack = []
        self.max = float('-inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x > self.max:
            self.max = x

    def pop(self) -> int:
        v = self.stack.pop()
        if v == self.max:
            self.max = max(self.stack) if self.stack else float('-inf')
        return v

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        for i in reversed(range(len(self.stack))):
            if self.stack[i] == self.max:
                v = self.stack.pop(i)
                self.max = max(self.stack) if self.stack else float('-inf')
                return v


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()