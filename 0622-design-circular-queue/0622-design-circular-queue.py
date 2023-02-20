from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.start = self.size = 0
        self.cap = k
        self.qlock = Lock()
        
    def enQueue(self, value: int) -> bool:
        with self.qlock: 
            if self.isFull():
                return False

            self.data[(self.start + self.size) % self.cap] = value
            self.size += 1
        return True

    def deQueue(self) -> bool:
        with self.qlock:
            if self.isEmpty():
                return False

            self.start = (self.start + 1) % self.cap
            self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.data[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.data[(self.start + self.size - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()