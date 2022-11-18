class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def possible(guess):
            trips = 0
            for t in time:
                trips += guess // t
                if trips >= totalTrips:
                    return True
            return False
        
        lo, hi = 0, max(time) * totalTrips
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if possible(mid):
                hi = mid
            else:
                lo = mid
        return hi