class MyStack:

    def __init__(self):
        self.push_q = deque()
        self.pop_q = deque()

    def push(self, x: int) -> None:
        self.push_q.append(x)

    def pop(self) -> int:
        while len(self.push_q) > 1:
            self.pop_q.append(self.push_q.popleft())
        self.pop_q, self.push_q = self.push_q, self.pop_q
        return self.pop_q.popleft()

    def top(self) -> int:
        if self.pop_q:
            return self.pop_q[0]
        else:
            return self.push_q[-1]
        
    def empty(self) -> bool:
        return not self.push_q and not self.pop_q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()