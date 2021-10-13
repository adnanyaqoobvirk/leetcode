class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        combs = ['a', 'b', 'c']
        while len(combs[0]) != n:
            ncombs = []
            for comb in combs:
                for c in "abc":
                    if comb[-1] != c:
                        ncombs.append(comb + c)
            combs = ncombs
        return "" if len(combs) < k else combs[k - 1]
                
        