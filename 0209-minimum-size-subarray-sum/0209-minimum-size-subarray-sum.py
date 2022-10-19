class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        
        min_len = inf
        total = left = right = 0
        while right < n:
            total += nums[right]
            right += 1
            while left <= right and total >= target:
                min_len = min(min_len, right - left)
                total -= nums[left]
                left += 1
        return 0 if min_len == inf else min_len