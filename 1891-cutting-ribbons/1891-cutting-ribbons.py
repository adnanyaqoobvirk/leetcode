class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def possible(l):
            cuts = 0
            for r in ribbons:
                cuts += r // l
                if cuts >= k:
                    return True
            return False
        
        lo, hi = 1, max(ribbons) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if possible(mid):
                lo = mid
            else:
                hi = mid
        return lo if possible(lo) else 0