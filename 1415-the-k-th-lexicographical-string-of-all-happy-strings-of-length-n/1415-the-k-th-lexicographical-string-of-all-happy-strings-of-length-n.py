class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack() -> str:
            if len(comb) == n:
                combs[0] += 1
                if combs[0] == k:
                    return "".join(comb)
            else:
                for c in "abc":
                    if not comb or comb[-1] != c:
                        comb.append(c)
                        res = backtrack()
                        if res:
                            return res
                        comb.pop()
            return ""
        comb = []
        combs = [0]
        return backtrack()