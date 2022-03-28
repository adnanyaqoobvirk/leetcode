class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[lo] <= target or nums[lo] > nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[hi] >= target or nums[hi] < nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1