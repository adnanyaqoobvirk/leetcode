class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dp(left: int, right: int) -> int:
            i = left + n - 1 - right
            
            if i == m:
                return 0
            
            return max(
                nums[left] * multipliers[i] + dp(left + 1, right),
                nums[right] * multipliers[i] + dp(left, right - 1)
            )
        
        n, m = len(nums), len(multipliers)
        return dp(0, n - 1)