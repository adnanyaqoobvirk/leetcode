class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] - nums[0] - mid >= k:
                hi = mid
            else:
                lo = mid
        return k + nums[0] + lo