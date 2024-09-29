class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        @cache
        def dp(l: int, r: int, xr: int) -> int:
            if xr == 0:
                return 0

            if l > r or xr < 0:
                return inf
            
            return 1 + min(
                dp(l + 1, r, xr - nums[l]),
                dp(l, r - 1, xr - nums[r])
            )
        
        ans = dp(0, len(nums) - 1, x)
        return -1 if ans == inf else ans