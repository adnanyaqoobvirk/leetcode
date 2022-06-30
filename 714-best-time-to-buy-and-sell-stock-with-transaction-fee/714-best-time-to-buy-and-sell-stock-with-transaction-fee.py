class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def helper(pos: int, bought: int) -> int:
            if pos == n:
                return -inf
            
            if bought:
                return max(
                    prices[pos],
                    prices[pos] + helper(pos + 1, False),
                    helper(pos + 1, True)
                )
            else:
                return max(
                    -prices[pos] - fee + helper(pos + 1, True),
                    helper(pos + 1, False)
                )
        
        n = len(prices)
        ans = helper(0, 0)
        return 0 if ans < 0 else ans