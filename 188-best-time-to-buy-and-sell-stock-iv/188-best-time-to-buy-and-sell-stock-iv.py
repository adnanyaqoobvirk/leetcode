class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def helper(pos: int, bought: bool, t: int) -> int:
            if t == 0 or pos >= n:
                return 0
            
            buy_stock = 0
            if not bought:
                buy_stock = -prices[pos] + helper(pos + 1, True, t)
            
            skip = helper(pos + 1, bought, t)
            
            sell_stock = 0
            if bought:
                sell_stock = prices[pos] + helper(pos + 1, False, t - 1)
                
            return max(
                buy_stock,
                skip,
                sell_stock
            )
        
        n = len(prices)
        return helper(0, False, k)