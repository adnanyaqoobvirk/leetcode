class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        left = 0
        curr = sum(nums)
        min_len = inf
        for right in range(n):
            curr -= nums[right]
            while left <= right and curr < x:
                curr += nums[left]
                left += 1
            if curr == x:
                min_len = min(min_len, n - right + left - 1)
        return min_len if min_len != inf else -1