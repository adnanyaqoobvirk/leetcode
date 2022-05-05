class MyStack:

    def __init__(self):
        self.q = deque()
        self.t = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.t = x
        
    def pop(self) -> int:
        last = None
        for _ in range(len(self.q) - 1):
            last = self.q.popleft()
            self.q.append(last)
        self.t = last
        ans = self.q.popleft()
        return ans

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()