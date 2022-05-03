class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums, n = sorted(nums), len(nums)
        
        left = 0
        while left < n and nums[left] == sorted_nums[left]:
            left += 1
        
        right = n - 1
        while right > left and nums[right] == sorted_nums[right]:
            right -= 1
        
        return right - left + 1