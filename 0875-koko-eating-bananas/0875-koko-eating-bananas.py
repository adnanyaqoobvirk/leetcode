class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                if hours > h:
                    return False
            return True
        
        lo, hi = 0, max(piles)
        while lo + 1 < hi:
            guess = lo + (hi - lo) // 2
            
            if possible(guess):
                hi = guess
            else:
                lo = guess
        return hi