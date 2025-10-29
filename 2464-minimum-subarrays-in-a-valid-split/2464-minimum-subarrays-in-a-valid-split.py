class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        
        @cache
        def dp(i: int, j: int) -> int:
            if j >= n:
                return inf
            
            if gcd(nums[i], nums[j]) > 1:
                if j == n - 1:
                    return 1
                else:
                    return min(1 + dp(j + 1, j + 1), dp(i, j + 1))
            else:
                return dp(i, j + 1)
        
        n = len(nums)
        ans = dp(0, 0)
        return -1 if ans == inf else ans