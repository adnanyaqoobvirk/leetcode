class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def helper(pos: int, bought: bool) -> int:
            if pos == n:
                return 0
            
            do_nothing = helper(pos + 1, bought)
            
            if bought:
                do_something = prices[pos] + helper(pos + 1, False)
            else:
                do_something = helper(pos + 1, True) - prices[pos] - fee
            
            return max(
                do_nothing,
                do_something
            )
        n = len(prices)
        return helper(0, False)