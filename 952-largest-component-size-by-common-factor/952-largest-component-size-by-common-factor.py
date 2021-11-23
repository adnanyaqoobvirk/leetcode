class DisjoinSet:
    def __init__(self, n: int) -> None:
        self.nodes = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        
    def find(self, i: int) -> int:
        if self.nodes[i] != i:
            self.nodes[i] = self.find(self.nodes[i])
        return self.nodes[i]
    
    def union(self, x: int, y: int) -> int:
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return xp
        
        if self.size[xp] > self.size[yp]:
            xp, yp = yp, xp
        
        self.nodes[xp] = yp
        self.size[yp] += self.size[xp]
        return xp
    
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def primeFactors(a: int) -> List[int]:
            factor = 2
            prime_factors = []
            while a >= factor * factor:
                if a % factor == 0:
                    prime_factors.append(factor)
                    a = a // factor
                else:
                    factor += 1
            prime_factors.append(a)
            return prime_factors
        
        ds = DisjoinSet(max(nums))
        factor_map = {}
        for num in nums:
            pfs = list(set(primeFactors(num)))
            factor_map[num] = pfs[0]
            for i in range(len(pfs) - 1):
                ds.union(pfs[i], pfs[i + 1])
        
        counts = defaultdict(int)
        for num in nums:
            counts[ds.find(factor_map[num])] += 1
        return max(counts.values())