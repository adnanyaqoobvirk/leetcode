class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h
        
        lo, hi = 0, max(piles)
        while lo + 1 < hi:
            k = lo + hi >> 1
            if possible(k):
                hi = k
            else:
                lo = k
        return hi