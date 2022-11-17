class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        lo, hi = -1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] > nums[-1]:
                lo = mid
            else:
                hi = mid
        return nums[hi]