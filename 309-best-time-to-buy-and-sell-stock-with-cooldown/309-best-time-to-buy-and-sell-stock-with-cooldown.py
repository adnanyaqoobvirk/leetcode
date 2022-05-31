class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def recurse(pos: int, bought: int) -> int:
            if pos >= n:
                return 0
            
            return max(
                -prices[pos] + recurse(pos + 1, 1),
                recurse(pos + 1, bought),
                (prices[pos] + recurse(pos + 2, 0)) if bought else 0
            )
        
        n = len(prices)
        return recurse(0, 0)