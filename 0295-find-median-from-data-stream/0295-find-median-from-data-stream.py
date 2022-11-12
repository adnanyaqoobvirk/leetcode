from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        median = self.nums[len(self.nums) // 2]
        if len(self.nums) % 2 == 0:
            median = (median + self.nums[len(self.nums) // 2 - 1]) / 2
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()