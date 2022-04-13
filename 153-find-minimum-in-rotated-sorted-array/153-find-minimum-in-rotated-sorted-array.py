class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[lo] > nums[mid] or nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]