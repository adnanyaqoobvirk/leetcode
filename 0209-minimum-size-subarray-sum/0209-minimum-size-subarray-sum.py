class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, l, total = inf, 0, 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if ans == inf else ans