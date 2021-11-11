class StringIterator:
    digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    
    def __init__(self, compressedString: str):
        self.cs = compressedString
        self.count = self.pos = 0
        self.ch = " "
                
    def next(self) -> str:
        if self.count == 0:
            if self.pos >= len(self.cs):
                return " "
            
            self.ch = self.cs[self.pos]
            self.pos += 1
            count = ""
            while self.pos < len(self.cs) and self.cs[self.pos] in StringIterator.digits:
                count += self.cs[self.pos]
                self.pos += 1
            self.count = int(count) - 1
        else:
            self.count -= 1
            
        return self.ch

    def hasNext(self) -> bool:
        return self.pos < len(self.cs) or self.count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()