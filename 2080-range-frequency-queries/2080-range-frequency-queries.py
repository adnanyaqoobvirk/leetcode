class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.ftable = defaultdict(list)
        for i, num in enumerate(arr):
            self.ftable[num].append(i)
    
    def bisect_left(self, arr: List[int], v: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo >> 1)
            if arr[mid] < v:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def bisect_right(self, arr: List[int], v: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo >> 1)
            if arr[mid] > v:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def query(self, left: int, right: int, value: int) -> int:
        positions = self.ftable[value]
        if not positions:
            return 0
        
        return self.bisect_right(positions, right) - self.bisect_left(positions, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)