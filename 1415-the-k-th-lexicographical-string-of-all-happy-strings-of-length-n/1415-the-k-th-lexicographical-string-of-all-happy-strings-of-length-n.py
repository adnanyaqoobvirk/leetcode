class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack() -> None:
            if len(comb) == n:
                if happy[0] < k:
                    happy[0] += 1
                    happy[1] = "".join(comb)
            else:
                for c in "abc":
                    if not comb or c != comb[-1]:
                        comb.append(c)
                        backtrack()
                        comb.pop()
        comb = []
        happy = [0, None]
        backtrack()
        return "" if happy[0] != k else happy[1]
        