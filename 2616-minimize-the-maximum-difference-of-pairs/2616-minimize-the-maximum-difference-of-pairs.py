class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def valid(d: int) -> bool:
            cnt = i = 0
            while i < n:
                if nums[i + 1] - nums[i] <= d:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p
        
        n = len(nums) - 1
        nums.sort()
        
        lo, hi = -1, max(nums) - min(nums)
        while lo + 1 < hi:
            mid = lo + hi >> 1
            
            if valid(mid):
                hi = mid
            else:
                lo = mid
        return hi