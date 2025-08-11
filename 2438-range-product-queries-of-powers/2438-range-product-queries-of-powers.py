class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []
        pos = 0
        while n > 0:
            if n & 1:
                powers.append(1<<pos)
            n >>= 1
            pos += 1
        
        pprods = [1]
        prod = 1
        for p in powers:
            prod = prod * p
            pprods.append(prod)
        
        res = []
        for l, r in queries:
            qprod = pprods[r + 1] // pprods[l]
            res.append(qprod % MOD)

        return res