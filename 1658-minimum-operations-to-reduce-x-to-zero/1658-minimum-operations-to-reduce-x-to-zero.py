class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        k = sum(nums) - x
        left = prefix = 0
        max_len = -1
        for right in range(n):
            prefix += nums[right]
            while left <= right and prefix > k:
                prefix -= nums[left]
                left += 1
            if prefix == k:
                max_len = max(max_len, right - left + 1)
        return n - max_len if max_len != -1 else -1