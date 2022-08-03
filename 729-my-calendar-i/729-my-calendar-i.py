from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.ivs = SortedList()

    def book(self, start: int, end: int) -> bool:
        lo, hi = 0, len(self.ivs) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            istart, iend = self.ivs[mid]
            
            if iend <= start:
                lo = mid + 1
            else:
                hi = mid
                
        if lo != len(self.ivs):
            istart, iend = self.ivs[lo]
            if istart <= start < iend or istart < end <= iend or start <= istart < end:
                return False
                
        self.ivs.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)