class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(pos: int, product: int) -> None:
            if product > 1:
                for i in range(pos, len(factors)):
                    f = factors[i]
                    if f <= int(math.sqrt(product)) and product % f == 0:
                        ans.append(comb + [f, product // f])
                        comb.append(f)
                        backtrack(i, product // f)
                        comb.pop()
                    
        factors = []
        for f in range(2, int(math.sqrt(n)) + 1):
            if n % f == 0:
                factors.append(f)
        
        ans = []
        comb = []
        backtrack(0, n)
        return ans