class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def helper(num: int, remaining: int) -> int:
            if num == n or remaining < 0:
                return -inf
            
            if remaining == 0:
                return 1
            
            return max(
                num * helper(num, remaining - num),
                helper(num + 1, remaining)
            )
        return helper(1, n)