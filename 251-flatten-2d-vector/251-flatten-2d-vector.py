class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = [lst for lst in vec if lst]
        self.lst_no = 0
        self.pos = 0

    def next(self) -> int:
        v = self.vec[self.lst_no][self.pos]
        if self.pos + 1 == len(self.vec[self.lst_no]):
            self.lst_no += 1
            self.pos = 0
        else:
            self.pos += 1
        return v

    def hasNext(self) -> bool:
        return self.lst_no < len(self.vec) and self.pos < len(self.vec[self.lst_no])


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()