class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(pos: int, bought: int) -> int:
            if pos == n:
                return -inf
            
            if bought:
                return max(
                    prices[pos],
                    helper(pos + 1, True),
                    prices[pos] + helper(pos + 1, False)
                )
            else:
                return max(
                    -prices[pos] + helper(pos + 1, True),
                    helper(pos + 1, False)
                )
        n = len(prices)
        ans = helper(0, 0)
        return 0 if ans < 0 else ans