class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def possible(k):
            ops = 0
            for num in nums:
                ops += k - num
                if ops < 0:
                    return False
            return True
        
        lo, hi = -1, max(nums)
        while lo + 1 < hi:
            mid = lo + hi >> 1
            if possible(mid):
                hi = mid
            else:
                lo = mid
        return hi