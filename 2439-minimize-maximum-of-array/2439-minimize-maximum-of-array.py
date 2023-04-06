class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = total = 0
        for i in range(len(nums)):
            total += nums[i]
            ans = max(ans, ceil(total / (i + 1)))
        return ans