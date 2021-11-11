class StringIterator:

    def __init__(self, compressedString: str):
        self.chars = []
        
        digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        count = ""
        for c in reversed(compressedString):
            if c in digits:
                count = c + count
            else:
                self.chars.append([c, int(count)])
                count = ""
                
    def next(self) -> str:
        if self.chars:
            c, count = self.chars[-1]
            if count == 1:
                self.chars.pop()
            else:
                self.chars[-1][1] -= 1
            return c
        return " "

    def hasNext(self) -> bool:
        return self.chars


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()