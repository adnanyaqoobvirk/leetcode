class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        
        lo, hi = -1, len(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid
        
        if hi == len(nums) or nums[hi] != target:
            return ans
        else:
            ans[0] = hi
        
        lo, hi = -1, len(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid
        
        ans[1] = lo
        
        return ans