class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums: return ans
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo == len(nums) or nums[lo] != target:
            return ans
        ans[0] = lo
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target: 
                lo = mid + 1
            else:
                hi = mid - 1
        ans[1] = hi
        
        return ans