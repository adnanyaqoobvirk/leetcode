class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack() -> None:
            if len(comb) == n:
                happys.append("".join(comb))
            else:
                for c in "abc":
                    if not comb or c != comb[-1]:
                        comb.append(c)
                        backtrack()
                        comb.pop()
        comb = []
        happys = []
        backtrack()
        return "" if len(happys) < k else happys[k - 1]
        