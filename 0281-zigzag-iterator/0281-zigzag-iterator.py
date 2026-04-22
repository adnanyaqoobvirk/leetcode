class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.indices = [0, 0]
        self.curr_idx = 0

    def next(self) -> int:
        while self.indices[self.curr_idx] >= len(self.vectors[self.curr_idx]):
            self.curr_idx = (self.curr_idx + 1) % len(self.vectors)
        
        v = self.vectors[self.curr_idx][self.indices[self.curr_idx]]
        self.indices[self.curr_idx] += 1
        self.curr_idx = (self.curr_idx + 1) % len(self.vectors)
        return v

    def hasNext(self) -> bool:
        for i in range(len(self.vectors)):
            if self.indices[i] < len(self.vectors[i]):
                return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())