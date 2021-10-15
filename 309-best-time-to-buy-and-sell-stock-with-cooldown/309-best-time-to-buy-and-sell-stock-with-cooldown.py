class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def recurse(pos: int, price: int) -> int:
            if pos >= n:
                return 0
            
            return max(
                recurse(pos + 1, prices[pos]),
                recurse(pos + 1, price),
                (prices[pos] - price + recurse(pos + 2, -1)) if price > -1 else 0
            )
        
        n = len(prices)
        return recurse(0, -1)
