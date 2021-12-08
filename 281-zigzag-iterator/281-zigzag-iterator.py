class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1, self.v2 = v1, v2
        self.p1 = self.p2 = 0
        self.p1_turn = True

    def next(self) -> int:
        ans = None
        if self.p1_turn:
            if self.p1 < len(self.v1):
                ans = self.v1[self.p1]
                self.p1 += 1
            else:
                ans = self.v2[self.p2]
                self.p2 += 1
        else:
            if self.p2 < len(self.v2):
                ans = self.v2[self.p2]
                self.p2 += 1
            else:
                ans = self.v1[self.p1]
                self.p1 += 1
        self.p1_turn = not self.p1_turn
        return ans

    def hasNext(self) -> bool:
        return self.p1 < len(self.v1) or self.p2 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())