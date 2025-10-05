class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + hi >> 1

            left = -inf if mid == 0 else nums[mid - 1]
            right = -inf if mid == n - 1 else nums[mid + 1] 
            
            if left < nums[mid] > right:
                return mid
            elif left < nums[mid] < right:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1