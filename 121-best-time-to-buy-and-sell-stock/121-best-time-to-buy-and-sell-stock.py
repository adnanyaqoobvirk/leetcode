class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(pos: int, bought: int) -> int:
            if pos == n:
                return -inf
            
            if bought:
                return max(
                    prices[pos],
                    helper(pos + 1, True)
                )
            else:
                return max(
                    helper(pos + 1, False),
                    -prices[pos] + helper(pos + 1, True)
                )
        
        n = len(prices)
        ans = helper(0, 0)
        return 0 if ans < 0 else ans