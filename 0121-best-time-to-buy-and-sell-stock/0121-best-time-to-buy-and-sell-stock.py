class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i: int, bought: bool) -> int:
            if i >= n:
                return 0

            if bought:
                return max(prices[i], dp(i + 1, bought))
            else:
                return max(dp(i + 1, True) - prices[i], dp(i + 1, False))
        n = len(prices)
        return dp(0, False)