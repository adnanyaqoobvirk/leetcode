class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        else:
            return self.push_stack[0]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack