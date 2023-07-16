class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dmap = defaultdict(int)
        self.q = deque()
        
        for num in nums:
            self.dmap[num] += 1
            self.q.append(num)

    def showFirstUnique(self) -> int:
        while self.q and self.dmap[self.q[0]] > 1:
            self.q.popleft()
        
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.dmap[value] += 1
        if self.dmap[value] <= 1:
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)