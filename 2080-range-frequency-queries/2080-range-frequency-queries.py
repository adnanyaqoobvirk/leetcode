class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.ftable = defaultdict(list)
        for i, num in enumerate(arr):
            self.ftable[num].append(i)
    
    def query(self, left: int, right: int, value: int) -> int:
        positions = self.ftable[value]
        if not positions:
            return 0
        return bisect_right(positions, right) - bisect_left(positions, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)