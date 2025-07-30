class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAND = max(nums)
        ans = 0
        count = 0
        for num in nums:
            if num == maxAND:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        return max(ans, count)