class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start: int, product: int) -> None:
            if product > 1:
                for f in range(start, int(math.sqrt(product)) + 1):
                    if product % f == 0:
                        ans.append(comb + [f, product // f])
                        comb.append(f)
                        backtrack(f, product // f)
                        comb.pop()
        ans, comb = [], []
        backtrack(2, n)
        return ans