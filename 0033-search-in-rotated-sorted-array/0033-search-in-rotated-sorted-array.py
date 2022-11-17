class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = -1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] > nums[-1]:
                lo = mid
            else:
                hi = mid
        
        if target <= nums[-1]:
            lo, hi = hi - 1, len(nums) - 1
        else:
            lo, hi = -1, hi - 1
            
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < target:
                lo = mid
            else:
                hi = mid
        return -1 if nums[hi] != target else hi