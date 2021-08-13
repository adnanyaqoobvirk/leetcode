class OrderedStream:

    def __init__(self, n: int):
        self.chunk = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunk[idKey - 1] = value
        output = []
        for i, v in enumerate(self.chunk):
            if v is None:
                break
            if v != -1:
                output.append(v)
                self.chunk[i] = -1
        return output

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)