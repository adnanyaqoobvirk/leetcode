class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr_pos = 0
        self.stack_size = 0

    def visit(self, url: str) -> None:
        self.curr_pos += 1
        self.stack_size = self.curr_pos
        if self.curr_pos < len(self.stack):
            self.stack[self.curr_pos] = url
        else:
            self.stack.append(url)

    def back(self, steps: int) -> str:
        self.curr_pos = max(self.curr_pos - steps, 0)
        return self.stack[self.curr_pos]

    def forward(self, steps: int) -> str:
        self.curr_pos = min(self.curr_pos + steps, self.stack_size)
        return self.stack[self.curr_pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)