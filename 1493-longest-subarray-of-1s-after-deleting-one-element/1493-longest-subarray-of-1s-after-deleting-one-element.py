class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while l < r and zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            longest = max(longest, r - l)
        return longest