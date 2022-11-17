class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        last = len(nums) - 1
        lo, hi = -1, last
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if mid == last or nums[mid] < nums[mid + 1]:
                lo = mid
            else:
                hi = mid
        return hi