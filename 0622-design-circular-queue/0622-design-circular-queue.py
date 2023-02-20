class MyCircularQueue:

    def __init__(self, k: int):
        self.push_stack = []
        self.pop_stack = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.push_stack.append(value)
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.Front()
        self.pop_stack.pop()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack[-1]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        if not self.push_stack:
            return self.pop_stack[0]
        
        return self.push_stack[-1]

    def isEmpty(self) -> bool:
        return len(self.push_stack) + len(self.pop_stack) == 0

    def isFull(self) -> bool:
        return len(self.push_stack) + len(self.pop_stack) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()