class MinHeap:
    def __init__(self, arr):
        self.h = arr[::]
        for i in reversed(range(len(self.h))):
            self._siftDown(i)
    
    def _swap(self, l, r):
        self.h[l], self.h[r] = self.h[r], self.h[l]
        
    def _siftDown(self, i):
        n = len(self.h)
        l = i * 2 + 1
        while l < n:
            r = i * 2 + 2
            if r >= n or self.h[l] < self.h[r]:
                j = l
            else:
                j = r
            if self.h[j] < self.h[i]:
                self._swap(j, i)
                i = j
                l = i * 2 + 1
            else:
                break
                    
    def _siftUp(self, i):
        p = (i - 1) // 2
        while i > 0 and self.h[p] > self.h[i]:
            self._swap(p, i)
            i = p
            p = (i - 1) // 2
            
    def size(self):
        return len(self.h)
    
    def peek(self):
        return self.h[0]
        
    def push(self, val):
        self.h.append(val)
        self._siftUp(len(self.h) - 1)
        
    def pop(self):
        if len(self.h) == 1:
            self.h.pop()
        elif len(self.h) > 1:
            self._swap(0, len(self.h) - 1)
            self.h.pop()
            self._siftDown(0)
            
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = MinHeap(nums)

    def add(self, val: int) -> int:
        self.h.push(val)
        while self.h.size() > self.k:
            self.h.pop()
        return self.h.peek()
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)