class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        
        seen = {1}
        h = [1]
        
        for _ in range(n - 1):
            num = heappop(h)
            for f in factors:
                ugly = f * num
                if ugly not in seen:
                    heappush(h, ugly)
                    seen.add(ugly)
        return heappop(h)