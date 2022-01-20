class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bsearch(k: int) -> bool:
            hcount = 0
            for pile in piles:
                hcount += math.ceil(pile / k)
            return hcount <= h
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if bsearch(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo