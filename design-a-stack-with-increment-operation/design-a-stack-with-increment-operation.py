class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.increments = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if not self.stack: 
            return -1
        if len(self.stack) > 1:
            self.increments[-2] += self.increments[-1]
        return self.stack.pop() + self.increments.pop()

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.increments[min(k, len(self.stack)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)