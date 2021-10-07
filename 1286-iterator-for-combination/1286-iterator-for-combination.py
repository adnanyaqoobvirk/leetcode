class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def backtrack(pos: int) -> None:
            if len(comb) == combinationLength:
                self.combs.append("".join(comb))
            else:
                for i in range(pos, n):
                    comb.append(characters[i])
                    backtrack(i + 1)
                    comb.pop()
        n = len(characters)
        comb = []
        self.combs = []
        self.cpos = 0
        backtrack(0)

    def next(self) -> str:
        ans = self.combs[self.cpos]
        self.cpos += 1
        return ans

    def hasNext(self) -> bool:
        return self.cpos < len(self.combs)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()