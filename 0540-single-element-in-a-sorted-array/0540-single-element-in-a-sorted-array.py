class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = -1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if mid & 1:
                if nums[mid - 1] != nums[mid]:
                    hi = mid
                else:
                    lo = mid
            else:
                if nums[mid] != nums[mid + 1]:
                    hi = mid
                else:
                    lo = mid
        return nums[hi]