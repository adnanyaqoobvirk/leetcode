class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = l = 0
        for r in range(len(nums)):
            while l < r and abs(nums[r] - nums[l]) > 2:
                l += 1
            ans += r - l + 1
        return ans