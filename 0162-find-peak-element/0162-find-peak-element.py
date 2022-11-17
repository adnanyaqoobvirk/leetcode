class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-inf)
        
        lo, hi = -1, len(nums) - 2
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] < nums[mid + 1]:
                lo = mid
            else:
                hi = mid
        return hi