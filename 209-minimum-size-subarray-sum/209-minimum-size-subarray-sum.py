class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, ans = 0, len(nums) + 1
        for right in range(len(nums)):
            target -= nums[right]
            while target <= 0:
                ans = min(ans, right - left + 1)
                target += nums[left]
                left += 1
        return ans % (len(nums) + 1)
        