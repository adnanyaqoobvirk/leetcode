class MinStack:

    def __init__(self):
        self.mins = []
        self.values = []

    def push(self, val: int) -> None:
        self.mins.append(min(val, self.mins[-1] if self.mins else float('inf')))
        self.values.append(val)

    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()