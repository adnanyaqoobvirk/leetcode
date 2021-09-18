from threading import Semaphore

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.qsem = Semaphore(capacity)
        self.dqsem = Semaphore(0)
        self.q = deque()
        
    def enqueue(self, element: int) -> None:
        self.qsem.acquire()
        self.q.append(element)
        self.dqsem.release()
            
    def dequeue(self) -> int:
        self.dqsem.acquire()
        ans = self.q.popleft()
        self.qsem.release()
        return ans

    def size(self) -> int:
        return len(self.q)