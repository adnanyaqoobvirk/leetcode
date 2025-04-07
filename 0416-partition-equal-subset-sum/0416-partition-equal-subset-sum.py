class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i: int, t: int) -> bool:
            if t == half:
                return True
            if i >= n or t > half:
                return False
            return dp(i + 1, t + nums[i]) or dp(i + 1, t)
            
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        half = total // 2

        return dp(0, 0)