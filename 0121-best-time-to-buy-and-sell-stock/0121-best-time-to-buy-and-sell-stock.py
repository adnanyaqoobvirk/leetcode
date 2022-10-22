class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(i: int, bought: bool) -> int:
            if i >= n:
                return -inf
            
            if bought:
                return max(
                    prices[i],
                    helper(i + 1, True)
                )
            
            return max(
                helper(i + 1, False),
                helper(i + 1, True) - prices[i]
            )
        
        n = len(prices)
        ans = helper(0, False)
        return 0 if ans < 0 else ans