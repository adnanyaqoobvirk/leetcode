from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.vals = SortedList()

    def addNum(self, num: int) -> None:
        self.vals.add(num)

    def findMedian(self) -> float:
        mid = len(self.vals) // 2
        
        if len(self.vals) & 1:
            return self.vals[mid]
        else:
            return (self.vals[mid] + self.vals[mid - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()