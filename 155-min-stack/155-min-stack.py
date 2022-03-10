class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mins.append([val, 1])
        else:
            self.stack.append(val)
            if self.mins[-1][0] > val:
                self.mins.append([val, 1])
            elif self.mins[-1][0] == val:
                self.mins[-1][1] += 1

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1][0]:
            self.mins[-1][1] -= 1
            if self.mins[-1][1] == 0:
                self.mins.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()