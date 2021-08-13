class OrderedStream:

    def __init__(self, n: int):
        self.chunk = [None] * n
        self.pos = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunk[idKey - 1] = value
        output = []
        while self.pos < len(self.chunk) and self.chunk[self.pos] is not None:
            output.append(self.chunk[self.pos])
            self.pos += 1
        return output

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)