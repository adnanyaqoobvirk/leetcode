class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniques = {}
        self.duplicates = set()
        
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        if len(self.uniques) > 0:
            return next(iter(self.uniques))
        else:
            return -1
        
    def add(self, value: int) -> None:
        if value not in self.duplicates:
            if value in self.uniques:
                del self.uniques[value]
                self.duplicates.add(value)
            else:
                self.uniques[value] = True

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)