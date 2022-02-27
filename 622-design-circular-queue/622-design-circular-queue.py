class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k - 1
        self.q = [None] * k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.tail == self.k:
            self.tail = 0
        else:
            self.tail += 1
            
        self.q[self.tail] = value
        if self.head == -1:
            self.head = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            if self.head == self.k:
                self.head = 0
            else:
                self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail == self.k and self.head == 0) or self.tail + 1 == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()