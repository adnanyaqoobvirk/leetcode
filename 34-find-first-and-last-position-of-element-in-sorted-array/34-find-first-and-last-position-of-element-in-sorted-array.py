class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        
        right = hi - 1
        if right < 0 or nums[hi - 1] != target:
            return [-1, -1]

        lo = 0
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
                
        left = lo
        return [left, right]
            