class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == nums[lo]:
                lo += 1
            elif nums[mid] == nums[hi]:
                hi -= 1
            elif nums[mid] < nums[lo] or nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return min(nums[lo], nums[lo - 1])