class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(m: int) -> int:
            if m == 0:
                return 0
            elif m < 0:
                return inf
            else:
                ans = inf
                for c in coins:
                    ans = min(ans, dp(m - c) + 1)
                return ans
        ans = dp(amount)
        return -1 if ans == inf else ans