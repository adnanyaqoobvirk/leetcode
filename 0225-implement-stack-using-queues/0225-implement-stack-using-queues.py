class MyStack:

    def __init__(self):
        self.q = deque()
        self.t = None

    def push(self, x: int) -> None:
        self.t = x
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.t = self.q.popleft()
            self.q.append(self.t)
        return self.q.popleft()

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()