class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = [v1, v2]
        self.q = deque([[0, 0], [1, 0]])

    def next(self) -> int:
        while self.q:
            v, p = self.q.popleft()
            if p < len(self.vs[v]):
                self.q.append([v, p + 1])
                return self.vs[v][p]
                
    def hasNext(self) -> bool:
        for v, p in self.q:
            if p < len(self.vs[v]):
                return True
        return False
    
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())