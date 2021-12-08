class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = []
        self.q = deque()
        for v in [v1, v2]:
            if v:
                self.vs.append(v)
                self.q.append([len(self.q), 0])

    def next(self) -> int:
        if self.q:
            v, p = self.q.popleft()
            if p < len(self.vs[v]) - 1:
                self.q.append([v, p + 1])
            return self.vs[v][p]
                
    def hasNext(self) -> bool:
        return len(self.q) > 0
    
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())