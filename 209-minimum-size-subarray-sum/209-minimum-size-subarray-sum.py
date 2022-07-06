class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, ans, total = 0, len(nums) + 1, 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
        return ans % (len(nums) + 1)