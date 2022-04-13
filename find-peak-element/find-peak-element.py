class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo